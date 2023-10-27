
# 1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.
# ilkSayi=1
# ikinciSayi=1 
# fiboToplam=0
# liste=[ilkSayi,ikinciSayi]
# for i in range(2,20):
#     fiboToplam=ilkSayi+ikinciSayi
#     liste.append(fiboToplam)
#     ilkSayi=ikinciSayi
#     ikinciSayi=fiboToplam

# print(liste)



# 2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)
# alinanSayi=int(input("sayi giriniz"))

# def mukemmelSayiBul(sayi):
#     toplam=0
#     for i in range(1,sayi):
#         if(sayi%i == 0):
#             toplam +=i
#     if(sayi == toplam):
#         print("Mükemmel Sayidir.")
#     else:
#         print("Mükemmel Sayi Degildir")

# mukemmelSayiBul(alinanSayi)



# 3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.
#EBOB, iki ya da daha fazla doğal sayının ortak bölenleri içerisindeki en büyük olanına, EKOK ise bu sayıların tam olarak bölünebildiği en küçük doğal sayıya denir.
# sayi1=int(input("sayi1'i giriniz "))
# sayi2=int(input("sayi2'yi giriniz "))
# def ebobEkok(sayi1,sayi2):
#     if sayi1>sayi2:
#         kucukSayi=sayi2
#     else:
#         kucukSayi=sayi1
#     for i in range(1,kucukSayi+1):
#     #ortak bölen=ebob
#         if(sayi1%i==0) and (sayi2%i==0):
#             ebob=i
#     ekok=(sayi1*sayi2)/ebob
#     return ebob,ekok

# ebob,ekok=ebobEkok(sayi1,sayi2)

# print(f"ebob:{ebob},ekok:{ekok}")



# 4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.
#Asal sayılar, sadece kendisi ve 1 sayısına bölünebilen 1'den büyük pozitif tam sayılar biçiminde tanımlanırlar.
# sayi=int(input("Asal sayı kontrolü için lütfen bir sayi giriniz."))
# if sayi>1:  
#     for i in range(2,sayi):
#         if sayi%i==0:
#             print(f"{sayi}:asal sayi değildir")
#             break
#     else:
#         print(f"{sayi}:asal sayidir")
# else:
#     print(f"{sayi}:asal sayi değildir")

# 5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 
girilenSayi=int(input("sayi giriniz :"))
for i in range(2,girilenSayi):
    while girilenSayi%i==0:
        girilenSayi=girilenSayi/i
        print(f"asal çarpanı:{i}")


