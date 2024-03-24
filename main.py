import random
import math


class Bilgisayar():

    def __init__(self):

        self.hesap_makinesi_işlem = ""
        self.hava_durumu_işlem = ""
        self.dosya_işlem = ""
        self.hava_durumu_listesi = ""
        self.günler = ""
        self.hava_durumu_günlük = ""

    def Hesap_Makinesi(self):

        print("""
           # # # # # # # # # # # # # # # # # # # # # # #                                                
           # 1-Toplama            #  2- Çıkarma        #
           #                      #                    #
           # 3-Çarpma             #  4- Bölme          #                               
           #                      #                    #
           # 5-Mutlak Değer Alma  #  6-Faktöriyel Alma #
           #                      #                    #
           # 7-Logartima Alma     #  8-Üslü Alma       #                            
           #                      #                    #  
           # 9-Kök Alma           #  q-Çıkış Yapma     #
           # # # # # # # # # # # # # # # # # # # # # # #  
        """)

        while True:
            print()
            self.hesap_makinesi_işlem = input("Yapmak istediğiniz işlemi seçiniz.")
            print()

            if self.hesap_makinesi_işlem == "1":
                ilk_sayı, ikinci_sayı = eval(
                    input("Toplanacak sayı(ları) (eğer iki sayı varsa aralarında virgül olacak şekilde) giriniz."))
                print()
                sonuc = ilk_sayı + ikinci_sayı
                print("Sonuç: {}".format(sonuc))

            if self.hesap_makinesi_işlem == "2":
                ilk_sayı, ikinci_sayı = eval(
                    input("Çıkarılacak sayı(ları) (eğer iki sayı varsa aralarında virgül olacak şekilde) giriniz."))
                print()
                sonuc2 = ilk_sayı - ikinci_sayı
                print("Sonuç: {}".format(sonuc2))

            if self.hesap_makinesi_işlem == "3":
                ilk_sayı, ikinci_sayı = eval(
                    input("Çarpılacak sayı(ları) (eğer iki sayı varsa aralarında virgül olacak şekilde) giriniz."))
                print()
                sonuc3 = ilk_sayı * ikinci_sayı
                print("Sonuç: {}".format(sonuc3))

            if self.hesap_makinesi_işlem == "4":
                ilk_sayı, ikinci_sayı = eval(
                    input("Bölünecek sayı(ları) (eğer iki sayı varsa aralarında virgül olacak şekilde) giriniz."))
                print()
                sonuc4 = ilk_sayı / ikinci_sayı
                print("Sonuç: {}".format(sonuc4))

            if self.hesap_makinesi_işlem == "5":
                sayı = int(input("Mutlak değeri alınacak sayıyı giriniz."))
                print()
                sonuc5 = abs(sayı)
                print("Sonuç: {}".format(sonuc5))

            if self.hesap_makinesi_işlem == "6":
                sayı = int(input("Faktöriyeli hesaplanacak sayıyı giriniz."))
                print()
                sonuc6 = math.factorial(sayı)
                print("Sonuç: {}".format(sonuc6))

            if self.hesap_makinesi_işlem == "7":
                sayı, taban = eval(input(
                    "Logaritması alınacak sayının önce kendisini sonra tabanını (aralarında virgül olacak şekilde) giriniz."))
                sonuc7 = math.log(sayı, taban)
                sonuc7 = int(sonuc7)
                print("Sonuç: {}".format(sonuc7))

            if self.hesap_makinesi_işlem == "8":
                sayı, üslü = eval(input(
                    "Üslü alınacak sayının önce kendisini sonra üslü değerini (aralarında virgül olacak şekilde) giriniz."))
                print()
                sonuc8 = sayı ** üslü
                print("Sonuç: {}".format(sonuc8))

            if self.hesap_makinesi_işlem == "9":
                sayı = int(input("Kökü alınacak sayıyı giriniz."))
                sonuc9 = math.sqrt(sayı)
                sonuc9 = int(sonuc9)
                print("Sonuç: {}".format(sonuc9))
            if self.hesap_makinesi_işlem == "q":
                print("Hesap makinesinden çıkış yapılıyor...")
                print()
                break
        pass

    def Hava_Durumu(self):

        while True:

            self.hava_durumu_listesi = ["Güneşli", "Bulutlu", "Parçalı Bulutlu", "Yağmurlu", "Sisli", "Kar"]
            self.günler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar", "pazartesi",
                      "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"]

            self.hava_durumu_işlem = input("""
           # # # # # # # # # # # # # # # # # # # # # # # ## # # # # # # # # # # #
           #  Hava durumuna hoşgeldiniz. Günlük hava durumu öğrenmek için g'yi, #
           #  haftalık hava durumunu öğrenmek için h'ye,                        #
           #  çıkış yapmak için de q ya basınız.")                              #
           # # # # # # # # # # # # # # # # # # # # # # # ## # # # # # # # # # # #
            """)

            if self.hava_durumu_işlem == "g":

                while True:
                    self.hava_durumu_günlük = input(
                        "Lütfen öğrenmek istediğiniz günü giriniz. Çıkış yapmak için q ya basınız.")

                    if self.hava_durumu_günlük in self.günler:

                        print()
                        tahmin = random.choice(self.hava_durumu_listesi)
                        self.hava_durumu_günlük = self.hava_durumu_günlük.capitalize()
                        print("{} günkü hava durumu: {}".format(self.hava_durumu_günlük, tahmin))

                    else:
                        print()
                        print("Günlük hava durumundan çıkış yapılıyor...")
                        break

            if self.hava_durumu_işlem == "h":
                gün1 = random.choice(self.hava_durumu_listesi)
                gün2 = random.choice(self.hava_durumu_listesi)
                gün3 = random.choice(self.hava_durumu_listesi)
                gün4 = random.choice(self.hava_durumu_listesi)
                gün5 = random.choice(self.hava_durumu_listesi)
                gün6 = random.choice(self.hava_durumu_listesi)
                gün7 = random.choice(self.hava_durumu_listesi)

                print("""
                Pazartesi : {}
                Salı : {}
                Çarşamba : {}
                Perşembe : {}
                Cuma : {}
                Cumartesi : {}
                Pazar : {}
                """.format(gün1, gün2, gün3, gün4, gün5, gün6, gün7))

            if self.hava_durumu_işlem == "q":
                print("Hava durumundan çıkış yapılıyor...")
                print()
                break
        pass

    def MCWord(self):

        while True:

            self.dosya_işlem = input(
                """
                Yapmak istediğiniz işlemi seçiniz:

                1 - Dosyaya yazma

                2 - Dosyadaki tüm içeriği temizleme

                3 - Dosyanın içeriğini görme

                q - Word'den çıkış yapma

                """)

            if self.dosya_işlem == "1":

                file = open("metindosyası.txt", "w")

                başlık = input("Başlık giriniz.")
                büyük_başlık = başlık.upper()
                file.write("                   {}\n\n".format(büyük_başlık))

                while True:

                    yazım_metni = input("Satırı giriniz. Çıkmak için q ya basınız.")

                    if yazım_metni == "q":
                        print("Yazma işleminden çıkış yapılıyor.")
                        break

                    else:

                        file.write("{}\n".format(yazım_metni))

                file.close()

            if self.dosya_işlem == "2":
                file = open("metindosyası.txt", "w")
                file.close()

                print("Yazılan metinler siliniyor...")

            if self.dosya_işlem == "3":
                file = open("metindosyası.txt", "r")
                içerik = file.read()
                print("Dosyanın içeriği şu şekildedir:")
                print()
                print(içerik)
                file.close()

            if self.dosya_işlem == "q":
                print("Word uygulamasından çıkış yapılıyor...")
                print()
                break
        pass

print("""

1 - Hesap Makinesi

2 - Hava Durumu 

3 - Microsoft Word 

""")

while True:

    ana_işlem = input("""Bilgisayara hoşgeldiniz.Kullanabileceğiniz uygulamalar yukarıda belirtilmiştir. 
    Lütfen kullanmak istediğiniz uygulamayı seçiniz. Çıkış yapmak için de q ya basınız.""")

    if ana_işlem == "q":
        print("Bilgisayar kapatılıyor. İyi günlerd dileriz...")
        break

    elif ana_işlem == "1":
        bilgisayar = Bilgisayar()
        bilgisayar.Hesap_Makinesi()

    elif ana_işlem == "2":
        bilgisayar = Bilgisayar()
        bilgisayar.Hava_Durumu()

    elif ana_işlem == "3":
        bilgisayar = Bilgisayar()
        bilgisayar.MCWord()

    else:
        print("Geçersiz işlem girdiniz.")