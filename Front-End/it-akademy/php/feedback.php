<?php
	/*https://api.telegram.org/bot909109368:AAG96XBf_wrV1-nqiCKwoAemXUkVeKVGvDg/getUpdates*/
	
	 
	 
require_once('phpmailer/PHPMailerAutoload.php');
$mail = new PHPMailer;
$mail->CharSet = 'utf-8';

$name = $_POST['user_name'];
$phone = $_POST['user_phone'];
$email = $_POST['user_email'];

//$mail->SMTPDebug = 3;                               // Enable verbose debug output

if($name == '' || $phone == '' || $email == ''){
	echo "Заполните все данные!";
}
else{


$mail->isSMTP();                                      // Set mailer to use SMTP
$mail->Host = 'smtp.mail.ru';  																							// Specify main and backup SMTP servers
$mail->SMTPAuth = true;                               // Enable SMTP authentication
$mail->Username = 'omurbekov.myktybek@mail.ru'; // Ваш логин от почты с которой будут отправляться письма
$mail->Password = 'it-academy'; // Ваш пароль от почты с которой будут отправляться письма
$mail->SMTPSecure = 'ssl';                            // Enable TLS encryption, `ssl` also accepted
$mail->Port = 465; // TCP port to connect to / этот порт может отличаться у других провайдеров

$mail->setFrom('omurbekov.myktybek@mail.ru'); // от кого будет уходить письмо?
$mail->addAddress('myktybek0011@gmail.com');     // Кому будет уходить письмо 
//$mail->addAddress('ellen@example.com');               // Name is optional
//$mail->addReplyTo('info@example.com', 'Information');
//$mail->addCC('cc@example.com');
//$mail->addBCC('bcc@example.com');
//$mail->addAttachment('/var/tmp/file.tar.gz');         // Add attachments
//$mail->addAttachment('/tmp/image.jpg', 'new.jpg');    // Optional name
$mail->isHTML(true);                                  // Set email format to HTML

$mail->Subject = 'Заявка с тестового сайта';
$mail->Body    = '' .$name . ' оставил заявку, его телефон ' .$phone. '<br>Почта этого пользователя: ' .$email;
$mail->AltBody = '';
	

	

	$token = '909109368:AAG96XBf_wrV1-nqiCKwoAemXUkVeKVGvDg';
	$chat_id = '-358645678';
	$arr =  array(
		'Имя пользователя' =>$name ,
		'Телефон' =>$phone ,
		'Email' => $email
		 ); 

	foreach ($arr as $key => $value) {
		$txt .= "<b>".$key."</b> ".$value."%0A";
	};

	$sendTelegram = fopen("https://api.telegram.org/bot{$token}/sendMessage?chat_id={$chat_id}&parse_mode=html&text={$txt}", "r");
	if($sendTelegram){
		header('Location: it-academy.html');
	}else {
		echo "Error!!!";
	}

}

?>