# 25. Leia um valor informado pelo usuário. Exiba o tipo da variável lida. Verifique se é possível converter o valor para número real (float). Se for possível, exiba o resultado da divisão desse número por 2. Caso contrário, exiba: “Não numérico”.
v = input()
print(type(v))
if v.isdigit() == True:
    n = int(v)
    print(n / 2)
else:
    print("Não numérico")
