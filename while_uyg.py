# numbers = [1, 3, 5, 7, 9, 12, 19, 21]
#
# # Soru 1: numbers listesini while döngüsü ile ekrana yazdırın.
# sayac = 0
# while (sayac < len(numbers)):
#     if (sayac == len(numbers) - 1):
#         print(numbers[sayac], end="")
#     else:
#         print(numbers[sayac], end=" / ")
#     sayac += 1
#
# # Soru 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.
# print("")
# start = int(input("Başlangıç Değeri: "))
# finish = int(input("Bitiş Değeri: "))
# while (start <= finish):
#     if (start % 2 == 1):
#         print(start, end="-")
#     start += 1

# Soru 3: 1 - 100 arasındaki sayıları tersten yazdırın.
# sayac=100
# while(sayac>0):
# #     print(sayac,end="-")
# #     sayac-=1
#
# # Soru 4: Kullanıcıdan aldığınız 5 sayıyı ekranda sıralı şekilde yazdırın.
# numbers=[]
# i=0
# while i<5:
#     sayi = int(input("Sayı:"))
#     numbers.append(sayi)
#     i+=1
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)

# Soru 5: Kullanıdan alacağınız sınırsız ürün bilgisini ürünler listesinde saklayınız.
    # ürün sayısını kullanıcı belirleyecek.
    # dictionary listesi yapısı (name,price) şeklinde olsun.
    # ürün ekleme işlemi bittiğinde ürünleri ekrana while döngüsü ile yazdırın.

urunler=[]
adet = int(input("Kaç ürün eklenecek: "))
i = 0
while (i<adet):
    name = input("Ürün İsmi:")
    price = input("Ürün Fiyatı:")
    urunler.append({
        'name':name,
        'price':price

    })
    i+=1

for urun in urunler:
    print(f"Ürün Adı:{urun['name']} ve ürün fiyatı:{urun['price']}")