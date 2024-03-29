from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt

from sessions.decorators import sign_in_required
from spadetree.utils import add_csrf
from usermessages.forms import ReplyMessageForm

import json

@sign_in_required
def count(request):
    """Return unread message count."""
    n = request.user.profile.unread_message_count()
    data = {
        'count': n,
    }
    return HttpResponse(json.dumps(data), mimetype='application/json')

@sign_in_required
def detail(request, pk, format=None):
    """Detail view for messages from one user."""
    sender = get_object_or_404(User, pk=pk)
    # Messages sent by user and received by sender
    user_messages = request.user.profile.messages(
        sender=sender).order_by('created')
    received_messages = user_messages.filter(recipient=request.user, 
        sender=sender, viewed=False)
    # Mark all messages from sender viewed
    if received_messages:
        for msg in received_messages:
            msg.viewed = True
            msg.save()
    # Group messages by date
    if user_messages:
        if format and format == '.json':
            data = {
                'messages': [msg.to_json() for msg in user_messages],
            }
            return HttpResponse(json.dumps(data), mimetype='application/json')
        dates = sorted(set([msg.date() for msg in user_messages]),
            key=lambda x: datetime.strptime(x, '%b %d, %y'))
        days = []
        for day in dates:
            msgs = [msg for msg in user_messages if msg.date() == day]
            days.append((day, msgs))
        d = {
            'days': days,
            'form': ReplyMessageForm(),
            'sender': sender,
            'title': '%s Messages' % sender.profile.full_name(),
        } 
        return render(request, 'usermessages/detail.html', add_csrf(request, d))
    messages.warning(request, 'You have no messages from that user')
    return HttpResponseRedirect(reverse('usermessages.views.list'))

@sign_in_required
def list(request, format=None):
    """Display most recent message from all senders."""
    user_messages = request.user.profile.recent_messages()
    if format and format == '.json':
        data = {
            'messages': [msg.to_json() for msg in user_messages],
        }
        return HttpResponse(json.dumps(data), mimetype='application/json')
    d = {
        'objects': user_messages,
        'title': 'Messages',
    }
    return render(request, 'usermessages/list.html', d)

@sign_in_required
@csrf_exempt
def new(request, pk, format=None):
    """Create new message."""
    receiver = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            form = ReplyMessageForm(request.POST)
            message = form.save(commit=False)
            message.recipient = receiver
            message.sender    = request.user
            message.save()
            if message:
                if format and format == '.json':
                    data = {
                        'message': message.to_json(),
                    }
                elif request.is_ajax():
                    d = {
                        'form': ReplyMessageForm(),
                        'message': message,
                        'sender': receiver,
                    }
                    message_template = loader.get_template(
                        'usermessages/message.html')
                    reply_message_form = loader.get_template(
                        'usermessages/reply_message_form.html')
                    context = RequestContext(request, add_csrf(request, d))
                    data = {
                        'message_template': message_template.render(context),
                        'reply_message_form': reply_message_form.render(
                            context)
                    }
                if (format and format == '.json') or request.is_ajax():
                    return HttpResponse(json.dumps(data), 
                        mimetype='application/json')
                messages.success(request, 'Message sent')
    return HttpResponseRedirect(reverse('usermessages.views.detail',
        args=[receiver.pk]))