import sqlite3

baglanti = sqlite3.connect("ilkVeriTabanim.db")
cursor = baglanti.cursor()

def tablo_olustur():
    cursor.execute("create table if not exists ogrenci (isim TEXT, soyisim TEXT, no INTEGER)")
    baglanti.commit()

# tablo_olustur()

def veri_ekle():

    isim = input("isminizi giriniz: ")
    soyisim = input("soyisminizi giriniz: ")
    no = int(input("no giriniz: "))

    cursor.execute("insert into ogrenci Values(?,?,?)",(isim,soyisim,no))
    baglanti.commit()
    

veri_ekle()