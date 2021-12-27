import math
x,y,z = 2,5,107
numara = 1,5,7,10,6
#1- Kullanıcıdan aldığınız iki sayının çarpımı ile x,y,z toplamının farkı nedir?
a = int(input("Birinci sayı girin: "))
b= int(input("İkinci sayıyı girin: "))
mesaj = a * b+x+y+z
# #2- y nin x e kalansız bölümünü bulunuz.
# mesaj = y//x
# #3- (x,y,z) toplamının mod 3 ü nedir?
# mesaj = (x+y+z)%100
# #4- y nin x. kuvvetini hesaplayınız.
# y **=x
# mesaj=y
# #5- x *y, z = numara işlemine göre z nin küpü kaçtır.
# x,*y,z=numara
# z**=3
# mesaj=z
# #6- x, *y, z = numara işlemine göre y nin değerleri toplamı kaçtır?
# mesaj=x,y,z
# print(mesaj)
# mesaj = int(math.fsum(y[::]))
print(mesaj)
