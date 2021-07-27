# ini adalah project latihan game bercerita

jawab = input("apakah kamu sudah siap memulai petuangalangan? (iya/belum)")

if jawab.lower().strip() == "iya":
    print(20 * "=", "GAME HAS BEGUN", 20 * "=")
    jawab = input("Kamu terdampar di sebuah pulau yang tidak diketahui, apakah ingin berjalan atau diam?").lower().strip()
    if jawab.lower().strip() == "berjalan":
        jawab = input("Terdengar suara jeritan keras yang membuatmu takut, apakah kamu ingin menghampiri atau sembunyi?").lower().strip()
        if jawab.lower().strip() == "menghampiri":
            print("Kamu terkaget melihat banyak mayat dan seorang pembunuh didepanmu!!")
            print("\033[31m"+"GAME OVER!!"+"\033[0m")
        else :
            print("Pembunuh menghampiri dirimu dan membunuhmu")
            print("\033[31m"+"GAME OVER!!"+"\033[0m")
    else :
        jawab = input("Sebuah ombak besar datang menghampirimu, memanjat pohon atau pergi dengan kapalmu?").lower()
        if jawab.lower() == "memanjat pohon":
            print("Pohon yang kamu panjat tidak kuat menahan gelombang ombak!!")
            print("\033[31m"+"GAME OVER!!"+"\033[0m")
        else :
            print("kamu lupa bahwa kapalmu karam dan tidak bisa digunakan, kamu hanyut oleh ombak")
            print("\033[31m"+"GAME OVER!!"+"\033[0m")
else:
    print("Oke silahkan datang kembali!")