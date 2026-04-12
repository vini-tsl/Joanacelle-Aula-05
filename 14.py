# 14. Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é múltiplo”.
n = input()
c = int(n)
r = c % 3
if r == 0:
    print("Múltiplo de 3")
else:
    print("Não é múltiplo")
