mesaj = "Merhaba. Benim Adım Mustafa"
# mesaj =mesaj.upper() #Büyük harfe çevirme
# mesaj =mesaj.lower() #Küçük harf
# mesaj =mesaj.title() # Başlık Düzeni
# mesaj =mesaj.capitalize() #Cümle düzeni
# mesaj =mesaj.strip() #Baş ve sondaki boşluk karakterlerini kaldırma
# mesaj =mesaj.split() # değişken içindekileri boşluk karakterine göre parçalara ayırır.
#mesaj =mesaj.split('.') # değişken içindekileri nokta karakterine göre parçalara ayırır.
#mesaj='*'.join(mesaj) #Parçalanmış mesaj değişkenini tekrar birleştirir.
#print(mesaj)

# print(mesaj.find("Mustafa")) #Kelime arama fonksiyonu.
# # Dönen sonuç ilk karakterin numarasını verir. -1 dönerse bulunmamıştır.
#
# print(mesaj.startswith("M"))
# #startswith: verilen karaker ile mi başlıyor true veya false döner.
#
# print(mesaj.endswith("a"))
# #endswith: verilen karaker ile mi bitiyor true veya false döner.

# print(mesaj.replace("Mustafa","Ahmet")) #Karakter değiştirme metodu.
# print(mesaj.replace("ı","i").replace(" ",".")) #Aynı anda birden fazla kullanılabilir.
print(mesaj.center(50,"*"))
