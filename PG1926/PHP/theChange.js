function init() {
    var x = document.getElementById("Money");
    var result = document.getElementById("result");
    x.onkeyup = function(e) {
    var val = this.value*100;

    var BirLira = Math.floor(val/100);
    val = val%100;

    var ElliKurus = Math.floor(val/50);
    val = val%50;

    var YirmiBesKurus = Math.floor(val/25);
    val = val%25;

    var BesKurus = Math.floor(val/10);
    val = val%10;

    var OnKurus = Math.floor(val/5);
    val = val%5;

    var BirKurus = Math.floor(val/1);
    val = val%1;

    result.innerHTML = "1 Lira : " + BirLira + 
    "<br /><hr> 50 Kuruş : " + ElliKurus + 
    "<br /><hr> 25 Kuruş : " + YirmiBesKurus + 
    "<br /><hr> 10 Kuruş : " + BesKurus + 
    "<br /><hr> 5 Kuruş : " + OnKurus + 
    "<br /><hr> 1 Kuruş : " + BirKurus;
    }
}
window.onload = init;