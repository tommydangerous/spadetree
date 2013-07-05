from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from channels.models import Channel
from choices.models import ChoiceNote

class Notification(models.Model):
    action       = models.CharField(max_length=255)
    channel      = models.ForeignKey(Channel)
    choice_note  = models.ForeignKey(ChoiceNote, blank=True, null=True)
    created      = models.DateTimeField(auto_now_add=True)
    model        = models.CharField(max_length=255)
    user         = models.ForeignKey(User)
    users_viewed = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def choice_messages(self, action):
        profile = self.user.profile
        if profile.tutor:
            pronoun = 'your'
        elif profile.tutee:
            pronoun = 'the'
        messages = {
            'accept': 'accepted',
            'deny': 'denied',
            'new': 'added a note to',
            'update': 'updated',
        }
        if self.action == 'complete':
            return 'marked the %s for %s complete' % (self.model_link(),
                self.channel.choice.interest.name.title())
        else:
            return '%s %s %s for %s' % (messages.get(action), pronoun, 
                self.model_link(), self.channel.choice.interest.name.title())

    def created_date_string_long(self):
        """January 01, 2013."""
        return self.created.strftime('%B %d, %Y')

    def mark_viewed(self, user):
        """Mark notification viewed for user."""
        user_ids = self.users_viewed
        if user_ids:
            user_ids = [int(i) for i in user_ids.split(',')]
            if not self.viewed(user):
                user_ids.append(user.pk)
                self.users_viewed = ','.join([str(i) for i in user_ids])
        else:
            self.users_viewed = '%s' % user.pk
        self.save()

    def message(self):
        notification_messages = {
            'choice': self.choice_messages(self.action),
            'choice_note': self.choice_messages(self.action),
        }
        return notification_messages.get(self.model)

    def model_link(self):
        link = ''
        if self.model in ['choice', 'choice_note']:
            link = '<a href="%s">request</a>' % reverse('choices.views.detail',
                args=[self.channel.choice.pk])
        return link

    def time(self):
        time = self.created.strftime('%I:%M').lstrip('0')
        am_pm = self.created.strftime('%p').lower()
        return '%s %s' % (time, am_pm)

    def viewed(self, user):
        """Check to see if user has viewed this notification."""
        user_ids = self.users_viewed
        if user_ids:
            user_ids = [int(i) for i in user_ids.split(',')]
            if user.pk in user_ids:
                return True
        return False