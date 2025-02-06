print("Hata Yönetimi Başladı")

try:
    sayi1 = int(input("Birinci Sayıyı Giriniz: "))
    sayi1 = int(sayi1)

    sayi2 = int(input("İkinci Sayıyı Giriniz: "))
    sayi2 = int(sayi2)

    if(sayi2 == 0):
        raise RuntimeError("İkinci sayı 0 olamaz.")
        #throw

    print(f"Sonuç: {sayi1/sayi2}")

    print("hata yönetimi bitti")

except ZeroDivisionError as e:
    print(e)
    print("ikinci sayı 0 olamaz")

except RuntimeError as e:
    print(e)
    print("Runtime hatası oluştu")

except Exception as e:
    print(f"Bir hata oluştu: {e}")
 
except ValueError:
    print("Lütfen sadece sayı giriniz")

else:
    print("Herşey yolunda")
finally:
    print("Hata yönetimi bitti")