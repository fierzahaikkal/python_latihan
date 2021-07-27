# project choose job
#username.py

username_input = str(input("Please enter your username:"))

print("selamat datang " + username_input)

#memilih job yang akan dipakai
print("silahkan pilih job yang tersedia")
print("- knight")
print('- witch')
print("- assassins")
print("- priest")

#input job
job_input = str(input("anda memilih:"))

#achievement job
print("\033[1m" "*achievement unlocked:" + job_input + "\033[0m")

#knight deskripsi
if job_input == "knight":
  print("selamat anda adalah petualang dengan jiwa yang berani dan gagah")
  print("dimasa depan anda akan memimpin banyak kelompok petualang")
#poin status
  def poin (poin_stat) :
    poin_stat = 30
    print("point status awal anda: %d" % poin_stat)
    #strenght
    poin_str = 0
    strenght = int(input("STR:" ))
    bayar = strenght
    if strenght >= 1:
      bayar = poin_stat - strenght
    #vit
    poin_vit = 0
    vitality = int(input("VIT:"))
    bayar = vitality
    if vitality >= 1:
      bayar = poin_stat - vitality
    #intelligence
    poin_int = 0
    intelligence = int(input("INT:"))
    bayar = intelligence
    if intelligence >= 1:
      bayar = poin_stat - intelligence
    #dexterity
    poin_dex = 0
    dexterity = int(input("DEX:"))
    bayar = dexterity
    if dexterity >= 1:
      bayar = poin_stat - dexterity
    #lucky
    poin_luk = 0
    lucky = int(input("LUK:"))
    bayar = lucky
    if lucky >= 1:
      bayar = poin_stat - lucky
  poin(30)
#witch deskripsi
if job_input == "witch":
  print("Maniac sihir yang ditakuti para petualang")
  print("Ia dapat menggunakan berbagai sihir tingkat tinggi")
#poin status
  def poin (poin_stat) :
    poin_stat = 30
    print("point status awal anda: %d" % poin_stat)
    # strenght
    poin_str = 0
    strenght = int(input("STR:"))
    bayar = strenght
    if strenght >= 1:
      bayar = poin_stat - strenght
    # vit
    poin_vit = 0
    vitality = int(input("VIT:"))
    bayar = vitality
    if vitality >= 1:
      bayar = poin_stat - vitality
    # intelligence
    poin_int = 0
    intelligence = int(input("INT:"))
    bayar = intelligence
    if intelligence >= 1:
      bayar = poin_stat - intelligence
    # dexterity
    poin_dex = 0
    dexterity = int(input("DEX:"))
    bayar = dexterity
    if dexterity >= 1:
      bayar = poin_stat - dexterity
    # lucky
    poin_luk = 0
    lucky = int(input("LUK:"))
    bayar = lucky
    if lucky >= 1:
      bayar = poin_stat - lucky
  poin(30)

#assassins deskripsi
if job_input == "assassins":
  print("Pembunuh yang tampil dalam kegelapan bayangan")
  print("Ahli dalam serangan cepat dan menikam secara diam-diam")
#poin status
  def poin (poin_stat) :
    poin_stat = 30
    print("point status awal anda: %d" % poin_stat)
    # strenght
    poin_str = 0
    strenght = int(input("STR:"))
    bayar = strenght
    if strenght >= 1:
      bayar = poin_stat - strenght
    # vit
    poin_vit = 0
    vitality = int(input("VIT:"))
    bayar = vitality
    if vitality >= 1:
      bayar = poin_stat - vitality
    # intelligence
    poin_int = 0
    intelligence = int(input("INT:"))
    bayar = intelligence
    if intelligence >= 1:
      bayar = poin_stat - intelligence
    # dexterity
    poin_dex = 0
    dexterity = int(input("DEX:"))
    bayar = dexterity
    if dexterity >= 1:
      bayar = poin_stat - dexterity
    # lucky
    poin_luk = 0
    lucky = int(input("LUK:"))
    bayar = lucky
    if lucky >= 1:
      bayar = poin_stat - lucky
  poin(30)

#priest deskripsi
if job_input == "priest":
  print("Orang suci yang dapat menggunakan skill penyembuh tingkat tinggi")
  print("mereka adalah seorang petinggi dari kalangan pendeta")
#poin status
  def poin (poin_stat) :
    poin_stat = 30
    print("point status awal anda: %d" % poin_stat)
    # strenght
    poin_str = 0
    strenght = int(input("STR:"))
    bayar = strenght
    if strenght >= 1:
      bayar = poin_stat - strenght
    # vit
    poin_vit = 0
    vitality = int(input("VIT:"))
    bayar = vitality
    if vitality >= 1:
      bayar = poin_stat - vitality
    # intelligence
    poin_int = 0
    intelligence = int(input("INT:"))
    bayar = intelligence
    if intelligence >= 1:
      bayar = poin_stat - intelligence
    # dexterity
    poin_dex = 0
    dexterity = int(input("DEX:"))
    bayar = dexterity
    if dexterity >= 1:
      bayar = poin_stat - dexterity
    # lucky
    poin_luk = 0
    lucky = int(input("LUK:"))
    bayar = lucky
    if lucky >= 1:
      bayar = poin_stat - lucky
  poin(30)