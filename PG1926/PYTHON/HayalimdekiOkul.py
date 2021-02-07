"""
HAYALİMDEKİ OKUL YAPISI
Şimdi hayal gücünü zorlayacak bir uygulama yapacağız. 
Bir okul hayal etmeni istiyoruz. Bu okulun her şeyini düşünmelisin. 
Çalışan, sınıf özellikleri, okul özellikleri, öğretmen özellikleri,
 ders özellikleri vb. gibi. 
 
Neler Yapacağız ?
-Bir okulun tüm detayını düşünmelisin.
-Daha sonrasında okul adında bir sınıf oluşturup 
içerisinde düşündüğün özellikleri anlatmalısınız. 
-Daha sonrasında 3 farklı okul tanımlayarak sınıf içerisinde 
yer alan özelliklerini değiştirmelisin.
"""

class Okul():
    tip="eğitimkurumu"
    def __int__(self,okul_adi="deneme",ogretmen_sayisi=10,ogrenci_sayisi=10,sinif_sayisi=10,bina_sayisi=1):
        self.okul_adi = okul_adi
        self.ogretmen_sayisi = ogretmen_sayisi
        self.ogrenci_sayisi = ogrenci_sayisi
        self.sinif_sayisi = sinif_sayisi
        self.bina_sayisi = bina_sayisi
        
    Okul1 = Okul("Gazi",50,648,20,2)
    Okul2 = Okul("Ankara",80,1489,3)
    Okul3 = Okul("Başkent",20,60,1)
    
    Okullar = [okul1, okul2, okul3]
    
    for okul in Okullar:
        print (okul.okul_adi,okul.ogretmen_sayisi,okul.ogrenci_sayisi,okul.sinif_sayisi,okul.bina_sayisi)
    
    