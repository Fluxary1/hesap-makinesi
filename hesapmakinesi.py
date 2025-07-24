import time
sayi1 = int(input("Birinci sayıyı girebilirsiniz: "))
sayi2 = int(input("İkinci sayıyıyı girebilirsiniz: "))

islem = input("Yapmak istediğiniz işlemi seçiniz '+' '-' '*' '/': ")

if islem == '+':
    print("Toplamı: ", sayi1 + sayi2)
    time.sleep(3)
elif islem == '-':
    print("Sonucu:", sayi1 - sayi2)
    time.sleep(3)
elif islem == '*':
    print("Çarpımı: ", sayi1 * sayi2)
    time.sleep(3)
elif islem == '/':
    if sayi2 == 0:
        print("Bu işler böyle yürümüyor.")
    else:
        print("Bölümü: ", sayi1 / sayi2)
        time.sleep(3)
else:
    print("Lütfen geçerli bir işlem seçiniz")