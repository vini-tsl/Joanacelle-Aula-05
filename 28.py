# 28. Leia um valor informado pelo usuário. Verifique o tipo da variável; Caso seja possível interpretá-lo como um valor numérico: Se for um número inteiro, exiba o dobro; Caso seja um número real, exiba a metade; Caso não seja possível interpretar como número, exiba: “Tipo inválido”.
v = input()
print(type(v))
if "." in v:
        n = float(v)
        print(n / 2)
elif v.isdigit() == True:
    n = int(v)
    print(n * 2)
else:
    print("Tipo inválido")
