# 8. Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário, informe “Número inválido”.
n = float(input())
if n > 0:
    print(n ** 0.5)
else:
    print("Número inválido")
