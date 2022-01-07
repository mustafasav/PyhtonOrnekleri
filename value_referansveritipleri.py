#value tipler >> strings number
# x = 5
# y = 25
# x = y
# y=10
# print(x,y)

#referans tipler >>> listeler
a = ["bir",2,3,4]
b = ["bir",2,3,4]
a = b
b[1] = "iki"

#b listesinde eklenen değer a listesini de etkiler

print(a,b)