<!--
Crearé un login y una página para registrar a un nuevo usuario con los siguientes datos:
usuario y contraseña.


(login.html) Login 	  -> Si el usuario existe 	 -> ./index.html
(login.html) Login    -> Si el usuario no existe -> (login.html) Login
 registrar.html       -> Nuevo usuario           -> (login.html) Login

El login tendrá la opción para registrar.
Usar "estilos.css" en el ejercicio.

-->

<?php

$dbhost = "localhost";
$dbuser = "root";
$dbpass = "";
$dbname = "test";

$conn = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

if(!$conn)
{
	die("No hay conexion:" .mysqli_connect_error());
}
?>