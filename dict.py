#ini adalah project latihan membuat kamus
keyword = {
    "is": "Adalah\nkata sambung di dalam kalimat,\nfor ex: what is your name",
    "can": "Bisa,Kaleng\nBenda,adalah kata yang mengungkapkan kesanggupan seseorang\nfor ex: Can i Help you?",
    "what": "Apa\nkata ini dapat berubah seiring dengan keadaannya \nfor ex: What is difference between you and me?",
    "cant": "Tidak bisa\n adalah kata yang mengungkapkan ketidak sanggupan seseorang\nfor ex: I cant"
}

kata = str(input("Masukkan kata yang ingin dicari: "))
print(keyword.get(kata))