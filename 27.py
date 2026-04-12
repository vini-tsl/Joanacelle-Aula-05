# 27. Leia dois números informados pelo usuário. Se ambos forem positivos, calcule e exiba a soma entre eles Caso contrário, calcule e exiba o produto entre eles.
a = int(input())
b = int(input())
if a > 0 and b > 0:
    print(a + b)
else:
    print(a * b)
