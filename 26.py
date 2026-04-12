# 26. Leia um número inteiro. Classifique o número de acordo com as seguintes regras: Se for maior que 0:
# Se for menor que 10 → exiba: “Pequeno”; Se estiver entre 10 e 100 → exiba: “Médio”; Se for maior que 100 → exiba: “Grande”;
# Caso contrário, exiba: “Negativo ou zero”.
n = int(input())
if n > 0:
    if n < 10:
        print("Pequeno")
    elif n <= 100:
        print("Médio")
    else:
        print("Grande")
else:
    print("Negativo ou zero")
