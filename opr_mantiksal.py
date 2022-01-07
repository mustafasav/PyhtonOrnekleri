x =6
# sonuc = 5 < x < 10
# and : ve >>> Koşulların tümü gerçekleştirme şartıdır.
 # true and true = true
 # true and false = false
 # false and true = false
 # false and false = false
sonuc1 = x>5 and x<10

# or : veya >>> Koşullardan herhangi biri gerçekleşme şartıdır.
    # true or true = true
    # true or false = true
    # false or true = true
    # false or false = false
    # false or false or false or false or true = true
sonuc2 = x>5 or x<10
sonuc = (5>6 or 6>10 or 7>16) and 8>6
print("4 Koşullu Sonuç: ",sonuc)

# not: değil >>> Değilse
sonuc3 = not(x>5 and x<10)
print(sonuc3)

# not(true) >>> false
# not(false) >>> true