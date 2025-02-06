import random

class Hesap:
    
    def __init__(self, hesap_sahibinin_adi, tck, hesap_bakiyesi=0):
        self.hesap_sahibinin_adi = hesap_sahibinin_adi
        self.tck = tck
        self.__hesap_bakiyesi = hesap_bakiyesi
        self.hesap_numarasi = ''.join(str(random.randint(0, 9)) for _ in range(12))

    def para_yatir(self, miktar):
        if miktar > 0:
            self.__hesap_bakiyesi += miktar
            print(f"Hesaba {miktar} TL para yatirildi.\n")
        else:
            print("Lutfen para yatirmak icin 0'dan buyuk bir deger giriniz!")
        
    def para_cek(self, miktar):
        if miktar > self.__hesap_bakiyesi:
            print("Lutfen para cekmek icin hesap bakiyesine esit veya hesap bakiyesinden kucuk bir deger giriniz!")
        else:
            self.__hesap_bakiyesi -= miktar
            print(f"Hesaptan {miktar} TL para cekildi.\n")

    def bakiye_goster(self):
        print(f"Hesap Bakiyeniz: {self.__hesap_bakiyesi} TL'dir.\n")

    def hesap_bilgisi_goster(self):
        print(f"Hesap Sahibi: {self.hesap_sahibinin_adi}\nHesap Sahibinin TC Kimlik No: {self.tck}\nHesap Numarasi: {self.hesap_numarasi}\nHesap Bakiyesi: {self.__hesap_bakiyesi}\n")

    # getter ve setter functions kullanimi
    def get_hesap_bakiyesi(self):
        return self.__hesap_bakiyesi

    # isim değişebilir
    def set_hesap_sahibinin_adi(self, hesap_sahibinin_adi):
        self.hesap_sahibinin_adi = hesap_sahibinin_adi
    

class VadeliHesap(Hesap):
    
    def __init__(self, hesap_sahibinin_adi, tck, hesap_bakiyesi=0):
        super().__init__(hesap_sahibinin_adi, tck, hesap_bakiyesi)
        self.faiz_orani = 0.05

    def faiz_hesapla(self):
        faiz = self.get_hesap_bakiyesi() * self.faiz_orani
        print(f"Vadeli Hesabinizin Günlik Faiz Getirisi: {faiz} TL'dir.\n")

    # Polymorphism
    def para_cek(self, miktar):
        print("Not: Vadeli hesaptan cekilen para yarin hesabiniza dusecektir.\n")
        super().para_cek(miktar)
    
    def bakiye_goster(self):
        print(f"Vadeli Hesap Bakiyeniz: {self.get_hesap_bakiyesi()} TL'dir.\n")


class VadesizHesap(Hesap):
    
    def __init__(self, hesap_sahibinin_adi, tck, hesap_bakiyesi=0):
        super().__init__(hesap_sahibinin_adi, tck, hesap_bakiyesi)

    def bakiye_goster(self):
        print(f"Vadesiz Hesap Bakiyeniz: {self.get_hesap_bakiyesi()} TL'dir\n")

print("\n\n***********************************************************\n")

vadeli_hesap_1 = VadeliHesap("Pelin Nur Col", "987654321", 2000)
vadeli_hesap_1.hesap_bilgisi_goster()
vadeli_hesap_1.bakiye_goster()
vadeli_hesap_1.para_yatir(1000)
vadeli_hesap_1.bakiye_goster()
vadeli_hesap_1.para_cek(500)
vadeli_hesap_1.bakiye_goster()
vadeli_hesap_1.para_cek(600)
vadeli_hesap_1.bakiye_goster()
vadeli_hesap_1.faiz_hesapla()

print("***********************************************************\n")

vadesiz_hesap_1 = VadesizHesap("Selay Yirtimci", "123456789")
vadesiz_hesap_1.hesap_bilgisi_goster()
vadesiz_hesap_1.bakiye_goster()
vadesiz_hesap_1.para_yatir(1000)
vadesiz_hesap_1.bakiye_goster()
vadesiz_hesap_1.para_cek(400)
vadesiz_hesap_1.bakiye_goster()
vadesiz_hesap_1.para_cek(800)
vadesiz_hesap_1.bakiye_goster()
