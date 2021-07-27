# belajar bin

# bin adalah satuan bit yang tertulis dalam suatu angka di program

print(bin(2))  # mencetak binary dari angka dua
print(0b10)  # mengubah binary ke angka
binset = 53
print(bin(binset))  #mencetak binary dari variabel

# enkripsi simple binary - angka
print("\n", 10* "="+"BINARY-ANGKA"+10* "=")
data_bin = (input("masukkan bin dari sebuah angka : "))  #menginput nilai bin
hasil = int(data_bin,2)  # merubah binary menjadi angka integer dengan dikali 2
print("ini adalah angka dari bin yang diberikan : ", hasil)  # mencetak hasil

# enkripsi simple angka - binary
print("\n", 10* "="+"ANGKA-BINARY"+10* "=")
data_angka = int(input("masukkan angka yang ingin diubah: "))  #menginput angka
print("ini adalah bin dari angka yang diberikan: ", format(data_angka,'08b'))  #mencetak angka menjadi bin

#data umum
a = 10
b = 27
#operasi bitwise | (atau/OR) pada binary
print("\n", 10* "="+"OR"+10* "=")
c = a | b
print("Nilai a :",a,"," " Binary:", format(a,'08b'))
print("Nilai b :",b,"," " Binary:", format(b,'08b'))
print(30* "="+"(|)")
print("Nilai c :",c,"," " Binary:", format(c,'08b'))

# operasi bitwise & (dan/AND) pada binary
print("\n", 10* "="+"AND"+10* "=")
c = a & b
print("Nilai a :",a,"," " Binary:", format(a,'08b'))
print("Nilai b :",b,"," " Binary:", format(b,'08b'))
print(30* "="+"(&)")
print("Nilai c :",c,"," " Binary:", format(c,'08b'))

# operasi bitwise XOR (^) pada binary
print("\n", 10* "="+"XOR"+10* "=")
c = a ^ b
print("Nilai a :",a,"," " Binary:", format(a,'08b'))
print("Nilai b :",b,"," " Binary:", format(b,'08b'))
print(30* "="+"(^)")
print("Nilai c :",c,"," " Binary:", format(c,'08b'))

# operasi bitwise NOT (~) pada binary
print("\n", 10* "="+"NOT"+10* "=")
c = ~a
print("Nilai a :",a,"," " Binary:", format(a,'08b'))
print(30* "="+"(~)")
print("Nilai c :",c,"," " Binary:", format(c,'08b'))
d = 0b11111111111
print(30* "="+"(^)")
print("Nilai c :",a^d,"," " Binary:", format(a^d,'08b'))