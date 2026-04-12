# 29. Leia um número inteiro. Verifique se ele é múltiplo de 5; Se for: Se o número for maior que 50 → exiba: “Múltiplo alto”; Caso contrário → exiba: “Múltiplo baixo”; Caso não seja múltiplo de 5, exiba: “Não é múltiplo”.
n = int(input())
r = n % 5
if r == 0:
    if n > 50:
        print("Múltiplo alto")
    else:
        print("Múltiplo baixo")
else:
    print("Não é múltiplo")
