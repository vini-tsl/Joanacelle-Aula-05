# 16. Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado.
v = input()
print(type(v))
n = float(v)
if type(v) == int:
    print(n ** 2)

