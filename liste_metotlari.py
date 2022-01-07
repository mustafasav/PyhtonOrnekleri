numara=[5,10,-5,1,25,4,26,-5]
harf=["Ağrı","Erzurum","Konya","Çorum","Ağrı","Zonguldak"]
sonuc=min(numara) #Minimum
sonuc=max(numara) #Maksimum Değer
sonuc=min(harf)
sonuc = numara[3:6]
sonuc = numara[:3]
sonuc = numara[4:]
# numara.append(49) #Dizinin sonuna eleman ekleme
# numara.insert(3,55) #Dizinin belli bir konumuna eleman ekleme
# numara.insert(-1,100) #Dizinin en son elemanından (-1) önce ekler
# numara.pop() #Listenin son elemanını siler.
# print(numara)
# numara.pop(1) #Listenin 1. indexsindeki  elemanını siler.
# print(numara)
# numara.remove(25) #silinecek elemanı veriyoruz. İndex numarası değil.
# # print(numara)
# print(harf)
# harf.remove("s")
# print(harf)
numara.sort() #Küçükten büyüğe sıralama
print(numara)
harf.sort() #Alfabetik sıraya göre sıralama. Türkçe karakteri sona atar
print(harf)
numara.reverse() #Diziyi tersine çevirir.
print(numara)
print(numara.count(-5))
print(harf.count("Ağrı"))