

class Kitap:
    def __init__(self, ad, yazar, sayfa_sayisi, isbn):
        self.__ad = ad
        self.__yazar = yazar
        self.__sayfa_sayisi = sayfa_sayisi
        self.__isbn = isbn

    def get_ad(self):
        return self.__ad
    
    def get_yazar(self):
        return self.__yazar
    
    def get_sayfa_sayisi(self):
        return self.__sayfa_sayisi
    
    def get_isbn(self):
        return self.__isbn
    
    def __str__(self):
        return f"Kitap Adi: {self.__ad}\nYazar: {self.__yazar}\nSayfa Sayisi: {self.__sayfa_sayisi}\nISBN: {self.__isbn}"
    

class KitapZatenVarHatasi(Exception):
    def __init__(self, mesaj= "Bu ISBN numarasina sahip bir kitap zaten var."):
        super().__init__(mesaj)


class Kutuphane:
    
    def __init__(self):
        self.__kitaplar = {}

    def kitap_ekle(self, kitap):
        if kitap.get_isbn() in self.__kitaplar:
            raise KitapZatenVarHatasi()
        self.__kitaplar[kitap.get_isbn()] = kitap
        print(f"{kitap.get_ad()} isimli kitap eklendi.")

    def kitap_sil(self, isbn):
        if isbn in self.__kitaplar:
            silinen_kitap = self.__kitaplar.pop(isbn)
            print(f"{silinen_kitap.get_ad()} isimli kitap silindi.")
        else:
            print("Kitap bulunamadi.")
    
    def kitaplari_listele(self):
        if not self.__kitaplar:
            print("Kütüphanede kitap bulunmamaktadir.")
        else:
            print("\n*****************************************\n\nKütüphanedeki kitaplar:\n")
            for kitap in self.__kitaplar.values():
                print(kitap)
                print("\n")
            print("*****************************************\n")


try:
    kutuphane = Kutuphane()

    kitap1 = Kitap("1984", "George Orwell", 328, "9789750719362")
    kitap2 = Kitap("Hayvan Çiftliği", "George Orwell", 152, "9789750719363")
    kitap3 = Kitap("Sineklerin Tanrısı", "William Golding", 328, "9789750719364")
    kutuphane.kitap_ekle(kitap1)
    kutuphane.kitap_ekle(kitap2)
    kutuphane.kitap_ekle(kitap3)
    kutuphane.kitaplari_listele()
    kutuphane.kitap_sil("9789750719362")
    kutuphane.kitaplari_listele()
    kutuphane.kitap_ekle(kitap3)
    kutuphane.kitaplari_listele()
except Exception as e:
    print(f"Hata: {e}\n")

