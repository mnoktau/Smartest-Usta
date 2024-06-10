import random

def ana_bulucu():
    arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
    while True:
        random_number = random.choice(arr)
        if random_number == "0":
            return bulucu_ilk_sayi()

def bulucu_ilk_sayi():
    arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
    birA = random.choice(arr)
    return birA, bulucu_ikinci_sayi(birA)

def bulucu_ikinci_sayi(birA):
    arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
    sayar = 0
    ulasici = []

    while True:
        random_number2 = random.choice(arr)
        if random_number2 == "0" and sayar == 0:
            birB = birA
            return birB
        elif random_number2 == "0" and sayar != 0:
            return bulucu_ucuncu(ulasici, sayar)
        else:
            sayar += 1
            ulasici.append(random_number2)

def bulucu_ucuncu(ulasici, sayar):
    arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
    sayar2 = 0
    ulasici2 = []

    while True:
        random_number3 = random.choice(arr)
        if random_number3 == "0" and sayar2 == 0:
            birB = "0"
            return birB
        elif random_number3 == "0" and sayar2 != 0:
            birB = ulasici2[sayar2 - 1]
            return birB
        else:
            sayar2 += 1
            ulasici2.append(random_number3)

# 9 kez ana_bulucu fonksiyonunu çağır ve sonuçları sakla
sonuclar = []
for _ in range(10):
    sonuc = ana_bulucu()
    if sonuc:
        sonuclar.append(sonuc)

# Sonuçları liste olarak göster
sonuclar_dizisi = []
for birA, birB in sonuclar:
    sonuclar_dizisi.extend([birA, birB])

print(f"Sonuçlar: {sonuclar_dizisi}")

# Sonuçları birleştirerek tek bir string oluştur
birleştirilmiş_sayı = ''.join(item for demet in sonuclar for item in demet)


print("Tek bir sayı:", birleştirilmiş_sayı)

ilk_onsekiz_basamak = birleştirilmiş_sayı[:18]

print("İlk 18 basamak:", ilk_onsekiz_basamak)


sayi_str = str(ilk_onsekiz_basamak)
ayni_sayilar = []

for rakam in sayi_str:
    if sayi_str.count(rakam) == 2 and rakam not in ayni_sayilar:
        ayni_sayilar.append(rakam)

print("İçerisinde 2 tane aynı olan sayılar:", ayni_sayilar)

ilk_on_basamak = sayi_str[:10]
print("İlk 10 basamak:", ilk_on_basamak)

ayni_sayilar = []
for rakam in sayi_str:
    if sayi_str.count(rakam) == 2 and rakam not in ayni_sayilar:
        ayni_sayilar.append(rakam)


ilk_on_basamak = sayi_str[:10]

ayni_sayi_var_mi = all(rakam in ilk_on_basamak for rakam in ayni_sayilar)


for rakam in ilk_on_basamak:
    if ilk_on_basamak.count(rakam) == 2 and rakam not in ayni_sayilar:
        ayni_sayilar.append(rakam)


ayni_sayilar_sayi1 = set()
ayni_sayilar_sayi2 = set(ilk_on_basamak)

for rakam in sayi_str:
    if sayi_str.count(rakam) == 2:
        ayni_sayilar_sayi1.add(int(rakam))

for rakam in ilk_on_basamak:
    if ilk_on_basamak.count(rakam) == 2:
        ayni_sayilar_sayi2.add(int(rakam))

#print("İlk sayıda 2 tane bulunan rakamlar:", ayni_sayilar_sayi1)

# Sayının digitlerini küme haline getir
digitler = set(str(ilk_on_basamak))

# Dizideki elemanların her biri için kontrol et
for eleman in ayni_sayilar_sayi1:
    # Elemanın her bir rakamını kontrol et
    for rakam in str(eleman):
        # Eğer rakam sayının digitlerinde varsa, True döndür
        if rakam in digitler:
            #print("Var:", rakam)
            break

def ikinci_sayidaki_degeri_bul(sayi1, sayi2, hedef_sayi):
    ikinci_sayi_degerleri = []
    for hedef_rakam in hedef_sayi:
        # İlk sayıdaki hedef rakamın indekslerini bul
        indeksler = [index for index, value in enumerate(str(sayi1)) if value == str(hedef_rakam)]
        
        # İkinci sayıdaki ilgili indekslerdeki rakamları al
        ikinci_sayi_degerleri.extend([str(sayi2)[index] for index in indeksler])
    
    return ikinci_sayi_degerleri

sayi2 = 1122334455
sayi3 = 9988776655

sonuc = ikinci_sayidaki_degeri_bul(ilk_on_basamak, sayi2, ayni_sayilar_sayi1)
sonuc2 = ikinci_sayidaki_degeri_bul(ilk_on_basamak, sayi3, ayni_sayilar_sayi1)
#print("İkinci sayıdaki değerler:", sonuc)
#print("İkinci sayıdaki değerler:", sonuc2)



#print("Kesinlikle 2 tane olan bir sayı olmalı ve 2 tane olanların toplam sayısı tek sayıda olmalı.")
#print("sağ veya sol taraf incelenir.")
#print("Bir sağ Bir sol")
#print("Solun solu da incelenebilir. Veya sağın sağı.")
#print("Range atabilir.")
#print("0 ve 10 farklı sayılar olarak gelir.")
#print("4 yönlü incelenir, Sağ Ortadan başlar, Sol Ortadan başlar, Sağ Sağdan başlar, sol soldan başlar.")