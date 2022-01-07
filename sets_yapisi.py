meyve={"portakal","elma","muz"}
#print(meyve[3]) # set yapıları indexlenemez.
# #set yapısının elemanlarına ulaşmak için döngü kullanılır.
# for x in meyve:
#     print(x)
# sets yapıları sıralama yapılamaz.
meyve.add("Nar")
meyve.update(["Mango","Grayfurt","Fındık","elma"])
#Bir elemandan sadece bir defa ekler ikinciyi göndersek bile eklemez
liste=[1,2,3,1,4,4,5,2] #normal listelerde tekrarlı eleman olabilir.
#ancak bu listeyi sets haline getirirsek tekrarlayanları çıkaracaktır.

print(liste) #Sonuç: [1,2,3,1,4,4,5,2]
print(set(liste)) #Sonuç: {1, 2, 3, 4, 5}
#Listeler köşeli parantez ile tanımlanır []
#Sets listeler ise süslü parantez {}

#eleman kaldırma - silme işlemi
meyve.remove("muz")
meyve.discard("elma")
meyve.clear() #Tüm elemanlar silinir.
print(meyve)