# 12. Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.
a = int(input())
b = int(input())
print(a + b)
if a > b:
    print("Maior:", a)
elif b > a:
    print("Maior:", b)
else:
    print("Iguais")
