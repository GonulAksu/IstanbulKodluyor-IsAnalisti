import math
# 1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

# userSize=float(input('Lütfen boy ölçünüzü giriniz. ör 1.72'))
# userWeight=float(input('Lütfen ağırlığınzı giriniz.'))
# if userSize > 0 :
#     VKİ=userWeight/(userSize*userSize)
#     sonuc1=f"Vücut Kitle İndeksiniz : {VKİ}"
# else :
#     sonuc1="lütfen anlamlı değerler giriniz"



# 2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

# userSalary=float(input("Maaşınız "))
# raiseRate=float(input("Zam oranı "))
# growth=userSalary*(raiseRate/100)
# currentSalary =userSalary+growth
# sonuc2=f"Maaşınız:{userSalary}, Artan miktar: {growth}, Güncelmaaşınız: {currentSalary}"

# 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

# sayilar=[]
# sayi1=sayilar.append(int(input("lütfen 1.sayıyı giriniz ")))
# sayi2=sayilar.append(int(input("lütfen 2.sayıyı giriniz ")))
# sayi3=sayilar.append(int(input("lütfen 3.sayıyı giriniz ")))
# print(sayilar)
# sayilar.sort(reverse=True)
# print(sayilar)
# sonuc3=f"Girilen en büyük sayı:{sayilar[0]}"

# 4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

# yariCap=int(input("dairenin yarıçapını giriniz:"))
#sabit deger
# PI=3.14
# cevre=2*PI*yariCap
# alan=PI*pow(yariCap,2)
# sonuc4=f"Dairenin cevresi: {cevre} - Dairenin alanı: {alan}"


# 5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

#Palindrom Sayı: Bir palindrom, soldan sağa veya sağdan sola doğru okunduğunda aynı olan bir sayıdır. Örneğin, 12321 ve 4554 palindrom sayılardır, ancak 12345 palindrom değildir.
palindromSayisi=input("Bir sayi giriniz")
#String Slicing [başlangıçindex: bitişindex: -1(index numarasını sağdan başlatır)]
ters=palindromSayisi[::-1]
if palindromSayisi==ters :
    sonuc5=f"girilen sayı palindrom sayısıdır. Girilen sayi: {palindromSayisi} Tersi: {ters}"
else :
    sonuc5=f"girilen sayı palindrom sayısı değildir. sayi:{palindromSayisi}, tersi:{ters}"

print(sonuc5)