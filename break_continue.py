#
# #break kullanımı
# #Döngüyü durdurmak - kırmak amacıyla
# # name = "Mustafa"
# # for harf in name:
# #     if harf =='s': # gelen harf s ise döngüyü durdur-çık-kır...
# # #         break
# # #     print(harf)
# #
# #
# #
# # # continue kullanımı:
# # # Adım atlamak için: atla ve devam et...
# #
# # name2 = "Mustafa Sav"
# # for harf in name2:
# #     if harf =="u" or harf =="a": # gelen harf u veya a ise atla ve döngüye devam et....
# #         continue
# #     print(harf)
#
#
# x=0
# while x <5:
#     if(x==2):
#         break
#     print(x)
#     x+=1
#
# x = 0
# while x < 5:
#     x += 1
#     if (x == 2):
#         continue
#     print(x)

# Örnek: 1 - 100 e kadar tek sayıların toplamını continue komutunu kullanarak bulunuz.

sayac = 0
toplam=0
while (sayac<=100):
    sayac += 1
    if(sayac%2==0):
        continue
    toplam=toplam+sayac
print(toplam)