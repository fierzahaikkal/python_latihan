# ini adalah project latihan game bercerita dengan beberapa pilihan
biru = "\033[94m"
kuning = "\033[93m"
end = "\033[0m"
jawab = input("apakah kamu sudah siap memulai kisah cerita hidupmu? (iya/belum)")

if jawab.lower().strip() == "iya":
    print(20 * "=", "GAME HAS BEGUN", 20 * "=")
    print("Kamu adalah seorang lelaki berusia 17 tahun, Tahun ini adalah tahun terakhirmu di SMA")
    print("kamu merasa minder dengan temanmu karena belum pernah pacaran sekalipun")
    print("Ada seorang gadis yang kamu sukai, ia bernama Meyrella dan ia juga seorang primadona sekolah")
    print("Suatu keajaiban dikelas 12 ini kamu sekelas dengannya, dan kamu berniat untuk mendekatinya")
    print("suatu saat di jam istirahat sekolah, kamu melihat Meyrella sedang sendirian")
    a = print("a. pergi mendekati Meyrella")
    b = print("b. mengajak Meyrella pergi ke kantin bersama")
    c = print("menatap Meyrella secara diam diam dari kejauhan")
    jawab = input("Jawabanmu: ")
    if jawab == "a" :
        print("kamu pergi mendekati Meyrella untuk mengajaknya berbicara")
        print(biru + "Sendirian aja nanti kesambet kalo kata orang" + end)
        print(kuning + "Oh iya gapapa," + end)