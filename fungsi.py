#cara membuat fungsi pada python

def salam ():
  waktu = int(input("Jam berapa sekarang:"))
  if waktu >= 20:
        print("Good night, have a nice dream")
  elif waktu >= 16:
        print ("Good night")
  elif waktu >= 12:
        print("Good Afternoon, keep spirit")
  elif waktu >= 6:
        print("Good morning, have a nice day")
  else :
        print("Good morning, its too early")

salam()