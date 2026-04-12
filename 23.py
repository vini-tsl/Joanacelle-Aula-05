# 23. Leia três números inteiros informados pelo usuário. Exiba em ordem decrescente o resto da divisão por 3.
n1 = int(input())
n2 = int(input())
n3 = int(input())

r1 = n1 % 3
r2 = n2 % 3
r3 = n3 % 3

if r1 >= r2 and r1 >= r3:
    print(r1)
    if r2 >= r3:
        print(r2)
        print(r3)
    else:
        print(r3)
        print(r2)
elif r2 >= r1 and r2 >= r3:
    print(r2)
    if r1 >= r3:
        print(r1)
        print(r3)
    else:
        print(r3)
        print(r1)
else:
    print(r3)
    if r1 >= r2:
        print(r1)
        print(r2)
    else:
        print(r2)
        print(r1)
