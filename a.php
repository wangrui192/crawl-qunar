<?php

//Connecting to Redis server on localhost
$url = 'https://flight.qunar.com/twell/longwell?http%3A%2F%2Fwww.travelco.com%2FsearchArrivalAirport=%E4%B8%8A%E6%B5%B7&http%3A%2F%2Fwww.travelco.com%2FsearchDepartureAirport=%E6%88%90%E9%83%BD&http%3A%2F%2Fwww.travelco.com%2FsearchDepartureTime=2017-10-08&http%3A%2F%2Fwww.travelco.com%2FsearchReturnTime=2017-10-08&locale=zh&nextNDays=0&searchLangs=zh&searchType=OneWayFlight&tags=1&mergeFlag=0&xd=f1505889039689&wyf=RADIw15DeAI1wMYozG54%2B1YodPIiwI54RA5IwgeiP12Rwg14%7C1505889014556&ex_track=&from=qunarindex&isNewInterface=true';

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$result = curl_exec($ch);
$a = substr($result, 1, strlen($result) - 2);
curl_close($ch);
$flight_list = json_decode($a, true)['oneway_data']['priceInfo'];
$min_price = 1000;
$temp = [];
$price = [];
foreach ($flight_list as $key => $value) {
    if ($value['lowppr'] < $min_price) {
        $min_price = $value['lowppr'];
        $temp = $value;
        $temp['flight'] = $key;
    }
    $price[] = $value['lowppr'];
}
if ($min_price < 1000) {
    echo "need send email price is $min_price";
    sendMail(json_encode($temp));
    $result = system("python /mnt/hgfs/a.py");
    echo $result;
}
$a = min($price);
echo "the min current price is $a\n";
$date = date('Y-m-d H:i:s');
file_put_contents('/mnt/hgfs/price', "$date the min current price is $a\n", FILE_APPEND);
function sendMail($content) {
    $host = "smtp.exmail.qq.com";
    $port = "25";
    $username = "用户名";
    $password = "密码";
    $formemail = "发送者";
    $formname = "主题名";
    $to_emails = 'wangrui.a@yuewen.com';
    $subject = '性能监控报警';
    include("/mnt/hgfs/dev/ThinkPHP/Library/Vendor/Swift/swift_required.php");
    $smtp = new \Swift_SmtpTransport($host, $port);
    $smtp->setUsername($username);
    $smtp->setPassword($password);
    $mailer = new \Swift_Mailer($smtp);
    $message = \Swift_Message::newInstance($subject, $content, "text/html", "utf-8");
    $message->setFrom(array($formemail => $formname));
    $message->setTo($to_emails);//发送人

    $status = $mailer->send($message);
    echo $status;
}
