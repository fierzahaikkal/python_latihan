# ini adalah project latihan tebak angka

import random  # mengimpor statement bawaan

# membuat loop batas angka untuk memulai
batas = True  # ketika 'batas' bernilai benar
while batas :  # maka akan ditulis seperti dibawah ini untuk dibuat perulangannya (loop)
   angka = input("Masukkan batas atas angka untuk memulai: ")  # memasukkan angka

   if angka.isdigit():  # jika angka yang dimasukkan berupa digit, maka ditulis
       print("Oke Benar, Yuk kita lanjut!")  # mencetak
       angka = int(angka)  # merubah tipe angka menjadi integer
       batas = False  # perulangan menentukan 'batas' akan berhenti & berlanjut ke lain
   else :  # tapi jika batasnya masih salah, maka perulangan menentukan 'batas' tetap berlanjut
       print("Maaf masih salah, silahkan coba kembali!")  # mencetak

# membuat game tebak angka dengan batas angka yang kita masukkan
jawaban = random.randint(1,angka)  # sistem menentukan nomor secara acak

tebak = None  # tebak bernilai 'none' karena kita belum menebak sama sekali
dihitung = 1  # tiap tebakan (pengulangan tebakan) akan dihitung mulai dari 1

while tebak != jawaban:  # menulis pengulangan (loop) hingga tebakan sama seperti jawaban
    tebak = input('Masukkan angka antara 1 sampai ' + str(angka) + ": ")  #memasukkan tebakan
    if tebak.isdigit():  # jika tebakan berupa digit
        tebak = int(tebak)  # merubah tebakan menjadi integer

    if tebak == jawaban:  # saat tebakan sama seperti 'jawaban' maka
        print("Selamat jawaban kamu benar!")  # mencetak

    else :  # tetapi jika tidak sama maka
        print("Maaf, jawaban kamu belum tepat, silahkan coba kembali!")  # mencetak
        dihitung += 1  # menghitung setiap perulangan, diawali dari 1, (1+1), (1+1+1),dst

print("Kamu memerlukan", dihitung, 'kali untuk memjawab!')  # mencetak akhir
