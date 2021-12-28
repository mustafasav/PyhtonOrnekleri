# # key - value mantığı ile çalışır.
# # 41 =>> Kocaeli veya 34=>İstanbul gibi
#
# sehirler=["Kocaeli","İstanbul"]
# plakalar=[41,34]
# mesaj = plakalar[sehirler.index("İstanbul")]
# #print(plakalar["kocaeli"]) >>> 41 e götürmeyi sağlayan dictionay dir.
# #plakalar={"key":"value"}
# plakalar={"Kocaeli":41,"İstanbul":34,"Afyon":3}
# mesaj=plakalar["Kocaeli"]
# plakalar["Ankara"]=6
# plakalar["Afyon"]="Yeni Değer"
# mesaj=plakalar
# print(mesaj)

users={ #bir anahtara birden fazla değer atanabilir.
    "mustafasav": {
        "yas":36,
        "email":"mustafa@sav.com",
        "adres":"Afyon",
        "tel":"123456",
        "yetki":["Admin","User"],
     },
    "ahmetkaya":{
        "yas": 25,
        "email": "ahmet@sav.com",
        "adres": "Ankara",
         "tel":"123456",
        "yetki":["User"]
    }

}
print(users["mustafasav"]["yetki"])
print(len(users["mustafasav"]["yetki"]))