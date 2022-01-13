#class
class Person:

    #class attributes
    address="adres yok"

    #constructor (yapıcı metod)
    def __init__(self,name,year):
    #object attributes
        #class oluşturulduğunda olmasını istediğimiz bilgileri buraya yazabiliriz.

        self.name=name
        self.year=year
        print("İnit metodu çalıştı")
        #init metodu obje oluşunca çalışır.

    #methods


#object (intance)

p1 = Person(name="mustafa",year=1990) #Person classından p1 objesi tanımladık.
p2 = Person(year="emine",name=1995)

#güncelleme
p1.name="Sevinç"
p1.address="Afyonkarahisar"

#özellik nesnesine erişmek
print(f'P1: Name {p1.name} year {p1.year} adres {p1.address}')
print(f'P2: Name {p2.name} year {p2.year} adres {p2.address}')
#print(p1)
#print(p2)
#print(p1==p2) #aynı mı farklı mı obje olduğunu görmek amacıyla