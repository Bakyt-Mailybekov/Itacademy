 var control=1;
$(window).scroll(function(){

var topWindow = $(window).scrollTop(),height=200
	
    if(topWindow >= height && control==1){
		$('.count').each(function(){
			
				$(this).prop('Counter',0).animate({
					Counter:$(this).text()
				},{
					duration:2000,
					easing:'swing',
					step:function(now){
						$(this).text(Math.ceil(now));
					}
				});
			
		});
		control++;
	}

})


	
	
	
 

