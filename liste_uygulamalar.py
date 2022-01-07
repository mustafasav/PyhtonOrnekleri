#1- "Eleşkirt, Tutak, Taşlıçay, Diyadin" elemanlarına sahip dizi oluşturun.
ilce=["Doğubeyazıd","Eleşkirt","Tutak","Taşlıçay","Diyadin","Merkez"]

#2- Liste kaç elemanlıdır?
# print(len(ilce))
# #3- Listenin ilk ve son elemanı nedir?
# print(ilce[0],"---",ilce[len(ilce)-1])
# print(ilce[-1]) #Listenin tersten sırasına göre yazdırır. -1 en sondan birinci eleman demektir.
# # #4- Tutak değerini Hamur ile değiştirin
# # ilce[1]="Hamur"
# nerede=ilce.index("Tutak") #Aranan değer dizinin kaçıncı elemanı onu buluruz.
# print(nerede)
# ilce[nerede]="Hamur"

#5-Patnos elemanı dizinin bir elemanı mıdır?
mesaj="Patnos" in ilce

#6- Listenin -2 indeksindeki değer nedir?
mesaj=ilce[-2]
#7- Listenin ilk 2 elemanını yazdırın.
mesaj=ilce[:3]
mesaj=ilce[-2:]

#8- Listenin son iki elemanı yerine Patnos ve Doğubeyazıd değerlerini ekleyin
#ilce[-2:]=["Patnos","Doğubeyazıd"]
mesaj=ilce
#9- Listenin üzerine Iğdır, Van, Erzurum değerlerini ekleyiniz

mesaj=ilce+["Iğdır","Van","Erzurum"] #burada gecici olarak eklenir kalıcı olarak diziye eklenmez.

#10- Listenin son elemanını silin.
# del ilce[-1]
# mesaj=ilce
#11- Liste elemanlarını tersten yazdırın.
mesaj=ilce[::-1]

print(mesaj)
#12- AŞağıdaki verileri bir liste şeklinde saklayınız.
    #ogrenci1: Erdal Kaya 2000, (70,60,60)
    #ogrenci2: Ayşe Bozdağ 2001, (50,70,80)
    #ogrenci3: Erkan Beşdal 1988, (40,90,80)