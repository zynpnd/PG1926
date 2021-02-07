"""
SIFIRI TAŞI
Sıralama algoritmaları programlamanın kaderini değiştiren algoritmalardır.
Neler Yapacağız ?
1.	Kullanıcıdan bir sayı girdisi alacağız.
2.	Daha sonra sayıların yerlerini değiştirmemiz gerekiyor. 
Fakat sadece 0 sayısını değiştireceğiz.
3.	Sayıların sırasını bozmadan 0 sayılarını listenin başına taşımanız gerekmektedir. 
4.	Listenin son halini ekrana yazdırmalısınız.
Kısıtlamalar
Herhangi bir kısıtlama yoktur.
Çıkış formatı
[2,4,1,6,4,0,0]
[0,0,2,4,1,6,4]
"""
import numpy as np
arr = [int(item) for item in input("Sayilari giriniz ").split()]
zeros = [i for i in arr if i == 0]
arr = [i for i in arr if i != 0]
zeros.extend(arr)
print(zeros)