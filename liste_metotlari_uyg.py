isim=["Ali","Ayşe","Hakan","Deniz","Mert","Can","Adem","Çiğdem"]
dogum=[1998,2000,1988,1987]
mesaj=""
# 1- "Mustafa" ismini listenin sonuna ekleyiniz.
#isim.append("Mustafa")

# 2- "Sena" değerini listenin başına ekleyiniz.
# isim.insert(0,"Sena")

# 3- "Deniz" ismini listeden siliniz.
#isim.remove("Deniz") #Çıkarılacak elemanın kendisi verilir.
#isim.pop(3) #Çıkarılacak elemanın index numarası verilir.

# # 4 - "Mert" isminin indexi nedir?
# # nerede=isim.index("Mert")
# # print(nerede)
# # 5- "Ali" listenin bir elemanı mıdır?
# #print(f'Aranan Karakter {isim.count("Ali")} tane var')
# mesaj= "Ali" in isim #isim dizininde "Ali" karakterini arar. Sonuç True veya false döner

#
# # 6- Liste elemanlarını tersten yazdırın.
# mesaj=isim[::-1]
#
# # 7- Liste elemanlarını alfaetik olarak sıralayınız.
# isim.sort()
# mesaj=isim
# #8- dogum listesini büyükten küçüğe sıralayınız.
# dogum.sort() #dogum listesini küçükten büyüğe sıralama yapar.
# dogum.reverse() #dogum listesini tersten sıralar.
# #mesaj=dogum
# #9- meyveler="Elma,Armut,Portakal,Limon" karakter dizisini listeye çeviriniz.
# # meyveler="Elma,Armut,Portakal,Limon".split(",") #Karakter dizisini liste haline getirir.
# print(meyveler)
# mesaj=meyveler[2]
#10- dogum dizinin en küçük ve en büyük elemanını bulunuz.
# mesaj = f'Dizinin en büyük elemanı {max(dogum)} ve en küçük elemanı {min(dogum)}'
#11- dogum dizininde kaç tane 1988 vardır?
# mesaj="Doğum dizininde {} tane 1988 li vardır".format(dogum.count(1988))
# 12- dogum dizinin tüm elemanlarını siliniz.
# dogum.clear()
# mesaj=dogum
# Kullanıcıdan alacağınız 3 adet şehir ismini bir listede saklayınız.
sehirler = []
sehir=input("Şehir Giriniz: ")
sehirler.append(sehir)
sehir=input("Şehir Giriniz: ")
sehirler.append(sehir)
sehir=input("Şehir Giriniz: ")
sehirler.append(sehir)
print(sehirler)







