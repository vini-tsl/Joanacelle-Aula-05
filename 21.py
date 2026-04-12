# 21. Leia um número inteiro informado pelo usuário.Verifique se o número é positivo. Caso seja, analise se ele é múltiplo de 2 e de 3 ao mesmo tempo. Se atender a ambas as condições, exiba: “Múltiplo de 2 e 3”. Caso contrário, exiba: “Não atende”. Se o número não for positivo, exiba: “Número inválido”.
n = int(input())
r = n % 2
r2 = n % 3
if n > 0:
    if r == 0 and r2 == 0:
        print("Múltiplo de 2 e 3")
    else:
        print("Não atende")
else:
    print("Número inválido")
