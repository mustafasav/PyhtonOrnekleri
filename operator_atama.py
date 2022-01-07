# x = 10
# y = 15
# z = 25
#
a,b,c=5,10,15 #tek satırda sıralı atama operatörü
# a,b = b,a #Yer değiştirme a b değerini, b a değerini alır.
#
# print(a,b,c)

a = a + 5 # Arttırma operatörü
a+=5 #Arttırma operatörü a = a+5
a-=5 #Azaltma operatörü a = a-5
a*=5 # Çarpma operatörü a = a*5
a/=5 #Bölme işlemi a = a / 5
a %=5 # Mod işlemi a = a % 5
a//=5 #Tam bölme
a**=5 # a nın 5 inci kuvvetini alır.
a**=b # a nın b inci kuvvetini al.

tupleornek = 1, 2, 3,4,5
print(tupleornek)
print(type(tupleornek))
b,a,*c = tupleornek #*c a ve b den sonra kalanları dizi şeklinde alır.
#eğer *c yapmasaydık 3 den fazla eleman olduğu için hata verirdi.
print(a,b,c)
print(c[2]) #c yi dizi şeklinde sakladığı için index numarası ile ulaşabiliriz.


