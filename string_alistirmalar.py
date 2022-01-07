website="http://www.mustafasav.com"
konu="Python Kursu : Baştan Sona Python Programlama Rehberiniz..."

# 1 - konu karakter dizininde kaç karakter bulunmaktadır?
# 2 - website içinden www karakterlerini alın.
# 3 - website içinden com karakterlerini alın.
# 4 - konu içinden ilk 15 ve son 15 karakteri alın
# 5 - konu değişkeni içindeki karakterleri tersten yazdırın

# #Soru1:
# print("Konu Değişkeninde {} adet karakter bulunmaktadır.".format(len(konu)))
# karaktersayisi=len(konu)
# print(f"Konu Değişkeinde {karaktersayisi} adet karakter bulunmaktadır. ")
#
# #Soru2:
# print("Alınan Karakter:{k}".format(k=website[7:10]))
# print("Alınan Karakter:"+website[7:10])
#
# #Soru3:
# print("Alınan Karakter:"+website[22:25])
# karaktersayisi=int(len(website))
# print("Alınan Karakter:"+website[karaktersayisi-3:karaktersayisi])

# #Soru4:
# karaktersayisi=int(len(konu))
# # print("Baştan Alınan Karakter>>> "+konu[0:15])
# # print("Baştan Alınan Karakter>>> "+konu[:15])
# print("Sondan Alınan Karakter>>> "+konu[karaktersayisi-15:karaktersayisi])
#print(konu[-15:])

#Soru5:
# print(konu[::-1])


# Soru7: 'ABC' ifadesini yan yana 3 defa yazdır.
print("ABC "*3)