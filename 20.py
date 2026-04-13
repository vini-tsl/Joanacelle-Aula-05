# 20. Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo, mostre na tela o valor.
n = int(input())
if n >= 0 and n <= 100:
    print("Dentro do intervalo")
else:
    print(n)
