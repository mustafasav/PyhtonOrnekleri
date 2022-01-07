numbers=[1,2,3,4,5,6]

for number in numbers:
    print(number)



#Belli bir aralıkta for döngüsünü çalıştırmak
print("---------------------")
for sayac in range(1,10):
    print(sayac)

names = ["Mustafa","Emine","Rıdvan","Fatma"]
for name in names:
    print(f"Benim Adım {name}")

name = "Mustafa Sav"

for n in name:
    print(n)


liste = {(1,2),(3,4),(5,6)}
for a,b in liste:
    print(a,b)


d = {"k1":1,"k2":2,"k3":3}

for item in d.items():
    print(item[0], "--",item[1])

d2 = {"k1": 1, "k2": 2, "k3": 3}

for key,value in d2.items():
    print(key,"--",value)