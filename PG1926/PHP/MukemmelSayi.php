<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="ZEYNEP NİDA SARICAN">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <title>Mükemmel Sayı</title>
</head>

<body style="text-align: center; background-color:black; margin-top: 100px;">
    <form name="toplam">

        <div>
            <label for="mukemmelSayi"  style= "font-size: 40px ; color: #cfb49e ; ">
                Sorgulamak istediğiniz sayıyı giriniz:
            </label>
        </div>
        <br>

        <div >
            <input type="girilenSayi" id="sayi" style= "font-size: 50px ; height: 150px; width: 300px; background-color:#cfb49e; 
                                                         color: black; text-align-last: center; padding:30px 20px 30px 20px; border-radius:50px; " >
        </div>

        <div style="text-align: center;">
            <input type="submit" id="hesapla" value="HESAPLA" class="btn btn-outline-light btn-lg" style="padding:10px 10px 10px 10px; margin-top:20px;  border: 2px solid #cfb49e;">
        </div>
    </form>
    <br><br>

    <script>
        var btn = document.getElementById("hesapla");
        btn.onclick = function() {
            var i, j;
            var toplam = 0;
            var sayi = Number(document.getElementById("sayi").value);
            for (i = 1; i < sayi; i++) {
                if (sayi % i == 0) {
                    toplam += i;
                }
            }
            if (sayi == toplam) {
                alert("Girdiğiniz " + sayi + " sayısı bir Mükemmel Sayıdır");
            } else {
                alert("Girdiğiniz " + sayi + " sayısı bir Mükemmel Sayı Değildir");
            }
        }
    </script>
</body>

</html>