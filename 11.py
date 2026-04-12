# 11. Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par negativo”; Caso contrário → “Ímpar”.
n = int(input())
r = n % 2
if r == 0:
    if n > 0:
        print("Par positivo")
    elif n < 0:
        print("Par negativo")
    else:
        print("Par")
else:
    print("Ímpar")
