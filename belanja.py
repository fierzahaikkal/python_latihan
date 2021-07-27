# ini adalah sistem kasir belanja
b1 = "Baju Lebaran"
b2 = "Baju Koko"
k1 = "Kurma Masjid"
s1 = "Susu Bebelac"
s2 = "Sandal Jepit"
print("""
1. Baju Lebaran
2. Baju Koko
3. Kurma Masjid
4. Susu Bebelac
5. Sandal Jepit
""")
ulang = True
while ulang :
    item = str(input("Masukkan nomor barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))
    if item == "1":
        jumlah >= 0
        harga1 = 200000 * jumlah
        format_harga1 = f"{harga1:,}"
        ulang = False
        print(b1, "Rp", format_harga1)
        lanjut = str(input("Apakah Ingin lanjut: "))
        if lanjut == "ya" or "iya":
            ulang = True

        else :
            ulang = False

    elif item == "2":
        jumlah >= 0
        harga2 = 120000 * jumlah
        format_harga2 = f"{harga2:,}"
        ulang = False
        print(b2, "Rp", format_harga2)
        lanjut = str(input("Apakah Ingin lanjut: "))
        if lanjut == "ya":
            ulang = True

        else:
            ulang = False

    elif item == "3":
        jumlah >= 0
        harga3 = 110000 * jumlah
        format_harga3 = f"{harga3:,}"
        ulang = False
        print(k1, "Rp", format_harga3)
        lanjut = str(input("Apakah Ingin lanjut: "))
        if lanjut == "ya":
            ulang = True

        else:
            ulang = False

    elif item == "4":
        jumlah >= 0
        harga4 = 98000 * jumlah
        format_harga4 = f"{harga4:,}"
        ulang = False
        print(s1, "Rp", format_harga4)
        lanjut = str(input("Apakah Ingin lanjut: "))
        if lanjut == "ya":
            ulang = True

        else:
            ulang = False

    elif item == "5":
        jumlah >= 0
        harga5 = 120000 * jumlah
        format_harga5 = f"{harga5:,}"
        ulang = False
        print(s2, "Rp", format_harga5)
        lanjut = str(input("Apakah Ingin lanjut: "))
        if lanjut == "ya":
            ulang = True

        else:
            ulang = False

    else:
        print("salah")

total_harga = harga1 + harga2 + harga3 + harga4 + harga5
format_totharga = f"{total_harga:,}"
print("Baiklah! Total belanjaan anda senilai Rp.", format_totharga)