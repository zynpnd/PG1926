<?php
date_default_timezone_set("Europe/Istanbul");
echo "Time is : " , (date("H:i:s")) , "<br>";
$Message = date("H");

switch ($Message){
    case (06<=$Message && $Message<10):
        echo "Günaydın";
    break;
    case (10<=$Message && $Message<17):
        echo "İyi günler";
    break;
    case (17<=$Message && $Message<20):
        echo "İyi akşamlar";
    break;
    case (20<=$Message && $Message<24):
        echo "İyi geceler";
    break;
    case (00<=$Message && $Message<06):
        echo "Esenlikler dilerim";
    break;
}
?>