$(document).ready(function() {
  $('.lazy').lazyload({
    event: 'load',
    failure_limit: 50,
    skip_invisible: false
  });
  $('.lazyScroll').lazyload({
    failure_limit: 50,
    skip_invisible: false
  });
});