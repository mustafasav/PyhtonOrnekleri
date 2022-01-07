site="http://www.mustafasav.com"
# detay="Python Kursu: Baştan Sona Python Programlama Rehberi"
# #1- ' Hello World ' karakter dizindeki baştaki sondaki boşluğu silin.
# # mesaj=" Hello World "
# # print(mesaj.strip())
# #2 "www.mustafasav.com" içinde mustafasav dışındaki karakterleri silin
mesaj="www.mustafasav.com"
mesaj=mesaj.lstrip(".w") #Soldan verilen karakterleri siler. her karakteri bir kere veriyoruz.
mesaj=mesaj.rstrip("moc.") #sağdan verilen karakterleri siler. karışık verilebilir.
mesaj="www.mustafasav.com"
mesaj=mesaj.strip("w.com")
# print(yenimesaj)
# #3 detay dizinin tümünü küçük yap:
# print(detay.lower())
# #4- site isminde kaç tane a karakteri var.
# # print(site.count("a"))
# #soru5: site www ile başlayıp .com ile mi bitiyor.
# if site.find("www") and site.endswith(".com"):
#     print("www ile başlayıp .com ile bitiyor")
#
#
print(mesaj)