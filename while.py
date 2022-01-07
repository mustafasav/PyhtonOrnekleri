x =0
while x <= 10:
    if x%2==1:
        print(f"Sayı Tek: {x}")
    else:
        print(f"Sayı Çift: {x}")
    x+=1


name = "" # False demek
while not name: #not name name girilinceye kadar demek yani true dönene kadar
    name =input("İsminizi Girin:")

print(f"Merhaba, {name}")