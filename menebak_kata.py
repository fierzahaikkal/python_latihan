# ini adalah project latihan tebak kata

bold = '\033[1m'
hijau = '\033[92m'
akhir = '\033[0m'

print(20*" ","PERMAINAN KATA", 20*" ")
print(bold + "jawablah kata yang berwarna hijau dengan tepat!" + akhir)
print('Mawar itu', hijau + "[WARNA]" + akhir)
print('Saya itu', hijau + "[KARATERISTIK]" + akhir)
print('Kita itu cuma ', hijau + "[HUBUNGAN]" + akhir)

print("\n",10*"=","JAWABAN", 10*"=")
warna = input("WARNA: ")
karakteristik = input("KARAKTERISTIK: ")
sifat = input("HUBUNGAN: ")

print("\n",10*"=","HASIL", 10*"=")
print('Mawar itu', bold + warna + akhir)
print('Saya itu', bold + karakteristik + akhir)
print('Kita itu cuma', bold + sifat + akhir)
