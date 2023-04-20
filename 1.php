<?php

$nombre = $_POST['nombre'];
$email = $_POST['Gmail'];
$telefono = $_POST['telefono'];
$tconsulta = $_POST['tconsulta'];
$consulta = $_POST['consulta'];

$formcontent="
    Nombre: $nombre \n
    Correo electronico: $email \n
    Telefono: $telefono \n
    Tipo de consulta: $tconsulta \n
    Consulta: $consulta.
";

$recipient = "veterinariahuellas@hotmail.com, veterinariahuellas@gmail.com";

$subject = "Consulta via web | Veterinaria Huellas de $nombre";

$header = "From: $email \r\n";
$header .= "Content-Type: text/plain; charset=UTF-8";
mail($recipient, $subject, $formcontent, $header) or die("Error!");
header("Location: index.html");

?>