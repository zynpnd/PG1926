"""
FizzBuzz
Yurt dışında işe girmek isteyen Toprak’a mülakatta sorulan bir soruyu cevaplaması gerekiyor. 
Sordukları soru FizzBuzz sorusudur. Bir türlü algoritmayı kuramayan Toprak için soruyu çözmelisin.
Fizzbuzz aslında başlangıcı ve sonu verilen iki sayı arasındaki tüm sayıları ekrana yazdırmaktır. 
Fakat ufak bir kurala bağlıdır. Eğer sayı üçe tam bölünüyorsa sayı yerine Fizz, 
eğer sayı beş’e tam bölünüyorsa Buzz, eğer her iki sayıya da tam bölünüyorsa ekrana FizzBuzz yazacaktır.
istenilen ekran çıktısı: 
1,2,Fizz,4,Buzz,Fizz,7,8,Buzz,Fizz,11,Fizz,13,14,FizzBuzz,16,17…
"""



sayi1=int(input("ilk sayiyi giriniz:"))
sayi2=int(input("sonuncu sayiyi giriniz:"))

for i in range(sayi1,sayi2):
    if i % 3 == 0 and i %5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)