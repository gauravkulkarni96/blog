$(window).scroll(function() {
   var hT = $('#skills').offset().top,
       hH = $('#skills').outerHeight(),
       wH = $(window).height(),
       wS = $(this).scrollTop();

   if (wS > (hT+hH-wH-500)){
      jQuery(document).ready(function(){
      	jQuery('.skillbar').each(function(){
      		jQuery(this).find('.skillbar-bar').animate({
      			width:jQuery(this).attr('data-percent')
      		},3000);
      	});
      });
    }
  });

  // $(document).ready(function(){
  //     $(this).scrollTop(0);
  // });
