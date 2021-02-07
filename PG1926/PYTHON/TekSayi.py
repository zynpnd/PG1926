"""
TEK SAYI GÜNCELLEME
Basit bir problem seti ile devam edelim. 
Şimdi listeler ile uğraşmaya devam ediyoruz. 
Şimdi dizideki en büyük tek sayıyı ekrana yazdırmalıyız.
NASIL ÇALIŞACAK?
1.	İlk olarak kullanıcıdan liste alalım.
2.	Daha sonrasında ise listenin içerisindeki en büyük tek sayıyı ekrana yazdırmalısın.
Örnek:
[0,1,2,3,4,5,6,7,8,9]
Çıktı:
[9]
"""


import pandas as pd

lst= []
lst=[int(item) for item in input("Lütfen Sayilari giriniz : ").split()]
tek=[]
tek=[item for item in lst if item % 2!= 0]
print(max(tek))