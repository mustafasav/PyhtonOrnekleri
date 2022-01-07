a,b,c,d = 5,5,10,4
a=b         # Aktarma operatörü
a == b      # Karşılaştırma operatörü eşit mi? True veya False değeri döner.
#print(a==b) # a eşit mi b ye diye karşılaştırır. Sonuçta True veya False değerini yazdırır.

# # 1- Girilen 2 sayıdan büyük olanı bulunuz.
# a = int(input("Sayı 1: "))
# b = int(input("Sayı 2: "))
# print(type(a+b))
# print(a+b)

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalamasını bulunuz.
#   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı olsun.
# vize1 = float(input("Vize 1: "))
# vize2 = float(input("Vize 2: "))
# final = float (input("Final: "))
# ort = vize1 * 30 / 100 + vize2 * 30 /100 + final*40/100
# ort2 = vize1 * 0.3 + vize2 * 0.3 + final*0.4
# ort3 = (vize1 + vize2)*0.3 + final*0.4
# print(ort,ort2,ort3)
# # 3- Girilen sayının tek mi çift mi olduğunu bulunuz.
# sayi= int(input("Sayı Gir: "))
# kalan= sayi % 2
# print(sayi,kalan)
# if(kalan==1):
# #     print("Sayı tek sayıdır.")
# # else:
# #     print("Sayı Çift sayıdır")
# # 4- Girilen bir sayının negatif veya pozitif olduğunu bulunuz.
# sayi= int(input("Sayı Gir: "))
# if(sayi<0):
#     print("Negatif")
# else:
#     print("Pozitif")
# 5- Parola ve mail bilgisi isteyerek aşağıdaki bilgilerde karşılaştırıp yanlış bilgi veya doğru bilgi mesajı veriniz.
# email: mustafa@sav.com şifre: 123456

mail = input("Email Bilgisi: ")
sifre= input("Şifre Bilgisi: ")
if (mail=="mustafa@sav.com" and sifre=="123456"):
    print("Giriş başarılı...")
else:
    print("Giriş başarısız...")
