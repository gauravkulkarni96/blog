$(window).scroll(function() {
   var hT = $('#skills').offset().top,
       hH = $('#skills').outerHeight(),
       wH = $(window).height(),
       wS = $(this).scrollTop();

   if (wS > (hT+hH-wH-450)){
     console.log("ht" + hT);
     console.log(hH);
     console.log(wH);
     console.log("ws" + wS);
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
