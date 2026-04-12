# 19. Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença entre eles.
a = int(input())
b = int(input())
if a == b:
    print("Iguais")
else:
    print("Diferentes")
    r = a - b
    if r > 0:
        print(r)
    else:
        r = b - a
        print(r)