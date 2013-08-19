// Generated by CoffeeScript 1.6.3
(function() {
  $(document).ready(function() {
    var animateBorder, animateBorderBack, resizeInsideBlockerHeightForSlide1, resizeInsideBlockerHeightForSlide2, resizeInsideBlockerHeightForSlide3;
    animateBorder = function(e) {
      return e.animate({
        borderColor: 'rgb(255, 26, 0)'
      }, 1000);
    };
    animateBorderBack = function(e) {
      return e.animate({
        borderColor: 'transparent'
      }, 1000);
    };
    resizeInsideBlockerHeightForSlide1 = function() {
      return $('.tutorial .insideBlocker').height($('.slide1 .inside').height());
    };
    resizeInsideBlockerHeightForSlide2 = function() {
      return $('.tutorial .insideBlocker').height($('.slide2 .inside').height());
    };
    resizeInsideBlockerHeightForSlide3 = function() {
      return $('.tutorial .insideBlocker').height($('.slide3 .inside').height());
    };
    $(document).on('click', '.tutorial .slide1 .next', function() {
      var user;
      user = $('.tutorial #tutorialUserType').attr('class');
      if (user === 'tutee') {
        animateBorderBack($('.tutorial header .browse, \
        .tutorial .search .field input'));
      } else {
        animateBorderBack($('.tutorial .slide1 input, \
        .tutorial .aboutTutorTutorial'));
      }
      $('.slide1').fadeOut(100, function() {
        return $('.slide2').fadeIn(100, function() {
          if (user === 'tutee') {
            animateBorder($('.tutorial .userDetail .top .chooseTutor'));
          } else {
            animateBorder($('.tutorial header .browse, \
            .tutorial .search .field input'));
          }
          return resizeInsideBlockerHeightForSlide2();
        });
      });
      return false;
    });
    $(document).on('click', '.tutorial .slide2 .back', function() {
      var user;
      user = $('.tutorial #tutorialUserType').attr('class');
      if (user === 'tutee') {
        animateBorderBack($('.tutorial .userDetail .top .chooseTutor'));
      } else {
        animateBorderBack($('.tutorial header .browse, \
        .tutorial .search .field input'));
      }
      $('.slide2').fadeOut(100, function() {
        return $('.slide1').fadeIn(100, function() {
          if (user === 'tutee') {
            animateBorder($('.tutorial header .browse, \
            .tutorial .search .field input'));
          } else {
            animateBorder($('.tutorial .slide1 input, \
            .tutorial .aboutTutorTutorial'));
          }
          return resizeInsideBlockerHeightForSlide1();
        });
      });
      return false;
    });
    $(document).on('click', '.tutorial .slide2 .next', function() {
      var user;
      user = $('.tutorial #tutorialUserType').attr('class');
      if (user === 'tutee') {
        animateBorderBack($('.tutorial .userDetail .top .chooseTutor'));
      } else {
        animateBorderBack($('.tutorial header .browse, \
        .tutorial .search .field input'));
      }
      $('.slide2').fadeOut(100, function() {
        return $('.slide3').fadeIn(100, function() {
          if (user === 'tutee') {
            animateBorder($('.tutorial .slide3 input'));
          } else {
            animateBorder($('.tutorial .choices button'));
          }
          return resizeInsideBlockerHeightForSlide3();
        });
      });
      return false;
    });
    $(document).on('click', '.tutorial .slide3 .back', function() {
      var user;
      user = $('.tutorial #tutorialUserType').attr('class');
      if (user === 'tutee') {
        animateBorderBack($('.tutorial .slide3 input'));
      } else {
        animateBorderBack($('.tutorial .choices button'));
      }
      $('.slide3').fadeOut(100, function() {
        return $('.slide2').fadeIn(100, function() {
          if (user === 'tutee') {
            animateBorder($('.tutorial .userDetail .top .chooseTutor'));
          } else {
            animateBorder($('.tutorial header .browse, \
            .tutorial .search .field input'));
          }
          return resizeInsideBlockerHeightForSlide2();
        });
      });
      return false;
    });
    return $(document).on('click', '.tutorial .slide3 .next', function() {
      var redirect;
      $('.tutorial').fadeOut(100);
      redirect = $('.tutorial #redirect').attr('class');
      if (!redirect) {
        redirect = '';
      }
      window.location.href = redirect;
      return false;
    });
  });

}).call(this);
