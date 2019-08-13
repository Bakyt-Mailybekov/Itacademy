//navbar
$(document).on('click','ul li',function(){
	$(this).addClass('active').siblings().removeClass('active');
});


//statistics
var control=1;
$(window).scroll(function(){

var topWindow = $(window).scrollTop(),height=800;
	
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
});
//$(document).on('ul li',function(){
$(window).scroll(function(){
	var topWindow = $(window).scrollTop();
	if(topWindow <= 400){
		$('.first-home').addClass('active').siblings().removeClass('active');
	}else if(topWindow <= 1000){
		$('.second-about-us').addClass('active').siblings().removeClass('active');
	}else if(topWindow <= 1500){
		$('.third-st').addClass('active').siblings().removeClass('active');
	}else if(topWindow <= 2000){
		$('.fifth-work').addClass('active').siblings().removeClass('active');
	}else if(topWindow <= 2400){
		$('.sixth-contacts').addClass('active').siblings().removeClass('active');
	}

});
//});

$('.menuShow-icon').click(function(){
	if($('.v-menu').is(':visible'))
		$('.v-menu').hide();
	else $('.v-menu').show();
});

$('.btn_blank').click(function(){
		 $('.first-block .conteiner-feedback').show();
});
$('.far').click(function(){
		 $('.first-block .conteiner-feedback').hide();
});



window.onresize = function(event){
	$('.v-menu').hide();
};







	
	
	
 

