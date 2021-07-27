#menginput nilai
nilai = int(input("Inputkan nilaimu: "))

if nilai >= 90: #(90,91,92....dst)
   grade = "A"
elif nilai >= 80: #(80,81,82....,89)
   grade = "B+"
elif nilai >= 70: #(70,71,72...,79)
   grade = "B"
elif nilai >= 60:
   grade = "C+"
elif nilai >= 50:
   grade = "C"
elif nilai >= 40:
   grade = "D"
else:
   grade = "E"

print("Grade: %s" % grade)

#perbedaan antara if dan elif adalah di range

# if, if >=n cth, if >= 90 (91,92,93...dst)

#elif n1=< elif <n2 cth

#if >= 90
#elif >=80 maka (80,81,82...,89)