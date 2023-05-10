<?php

$dbhost = "localhost";
$dbuser = "root";
$dbpass = "";
$dbname = "test";

$conn = mysqli_connect($dbhost, $dbuser, $dbpass, $dbname);
if (!$conn)
{
die ("No hay conexión: ".mysqli_connect_error());
}

$nombre = $_POST["Correo"]
$pass = $_POST["contraseña"]


$query = mysql_db_query($conn, "SELECT = FROM login WHERE usuario = '".$nombre."' and password = '".$pass."'");
$nr = mysqli_num_rows($query);
if ($nr == i)
{
//header("Location: C:\Users\Pokeomon\Desktop\Spa de veterinaria\Veterinaria\pages\Login.html")
echo "Bienvenido" .$nombre
}
else if ($nr == 0)
{

echo: "No ingresó";

}


?>