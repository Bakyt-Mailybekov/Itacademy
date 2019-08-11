<?php
	/*https://api.telegram.org/bot909109368:AAG96XBf_wrV1-nqiCKwoAemXUkVeKVGvDg/getUpdates*/

	$name = $_POST['user_name'];
	$phone = $_POST['user_phone'];
	$email = $_POST['user_email'];

	$token = '909109368:AAG96XBf_wrV1-nqiCKwoAemXUkVeKVGvDg';
	$chat_id = '-358645678';
	$arr =  array(
		'Имя пользователя' =>$name ,
		'Телефон' =>$phone ,
		'Email' => $email
		 ); 

	foreach ($arr as $key => $value) {
		$txt = "<b>".$key."</b> ".$value."%0A";
	};

	$sendTelegram = fopen("https://api.telegram.org/bot{$token}/sendMassage?chat_id={$chat_id}&parse_mode=html&text={$txt}", "r");
	if($sendTelegram){
		echo "Thank you!!!";
	}else {
		echo "Error!!!";
	}

	

?>