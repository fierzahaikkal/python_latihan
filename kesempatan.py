#ini adalah latihan perulangan for

times = 5

for kesempatan in range(times):
    konfirm = str(input("Apakah kamu ingin mengulang? "))
    if konfirm == "ya" or "iya" or "yes" or "y":
        times -= 1
        print("sisa kesempatan kamu adalah: "+ str(times))

        if times == 0:
            print("Kesempatan sudah habis, anda tidak bisa mengulang")
    else:
        print("Oke silahkan kembali nanti")