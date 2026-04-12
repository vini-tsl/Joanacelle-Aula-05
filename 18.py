# 18. Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro.
n = int(input())
r = n % 2
if n == 0:
    print("Neutro")
elif r == 0:
    if n > 0:
        print("Par positivo")
    else:
        print("Par negativo")
else:
    if n > 0:
        print("Impar positivo")
    else:
        print("Impar negativo")