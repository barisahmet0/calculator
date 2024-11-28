operator = input('Bir operator giriniz\n Toplama=+\n Çarpma=*\n Bölme=/\n Çıkarma=-\n ')
if operator =='+':
    girilecek_sayi = int(input('kaç sayı gireceksiniz : '))
    toplam = 0
    while True:
        sayi = float(input('bir sayı giriniz : '))
        girilecek_sayi -= 1
        toplam +=sayi
        if girilecek_sayi == 0:
            break
    print(toplam)
elif operator =='-':
    girilecek_sayi = float(input('kaç sayı gireceksiniz : '))
    fark = 0
    while True:
        sayi = float(input('bir sayı giriniz : '))
        girilecek_sayi -= 1
        sayi -=fark
        if girilecek_sayi == 0:
            break
    print(fark)
elif operator =='/':
    girilecek_sayi = int(input('kaç sayı gireceksiniz : '))
    bölüm = 1
    while True:
        sayi = float(input('bir sayı giriniz : '))
        girilecek_sayi -= 1
        sayi /=bölüm
        if girilecek_sayi == 0:
            break
    print(bölüm)
elif operator =='*':
    girilecek_sayi = int(input('kaç sayı gireceksiniz : '))
    çarpım = 1
    while True:
        sayi = int(input('bir sayı giriniz : '))
        girilecek_sayi -= 1
        çarpım *=sayi
        if girilecek_sayi == 0:
            break
    print(çarpım)