#ini adalah project latihan membuat calculator

num1 = float(input("Masukkan angka pertama: "))
opr = input("Masukkan tanda operasi: ")
num2 = float(input("Masukkan angka kedua: "))
print(30*"-", opr)

if opr == '+':
    print(num1+num2)
elif opr == '-':
    print(num1-num2)
elif opr == '*':
    print(num1*num2)
elif opr == '/':
    print(num1/num2)
elif opr == '%':
    print(num1%num2)
elif opr == '^':
    print(num1**num2)
else:
    print("Operasi yang dimasukkan salah")