n1 = float(input("Digite a 1ª nota (0 a 10): "))
while n1 < 0 or n1 > 10:
    print("Nota inválida. Digite novamente.")
    n1 = float(input("Digite a 1ª nota (0 a 10): "))

n2 = float(input("Digite a 2ª nota (0 a 10): "))
while n2 < 0 or n2 > 10:
    print("Nota inválida. Digite novamente.")
    n2 = float(input("Digite a 2ª nota (0 a 10): "))

n3 = float(input("Digite a 3ª nota (0 a 10): "))
while n3 < 0 or n3 > 10:
    print("Nota inválida. Digite novamente.")
    n3 = float(input("Digite a 3ª nota (0 a 10): "))

n4 = float(input("Digite a 4ª nota (0 a 10): "))
while n4 < 0 or n4 > 10:
    print("Nota inválida. Digite novamente.")
    n4 = float(input("Digite a 4ª nota (0 a 10): "))

n5 = float(input("Digite a 5ª nota (0 a 10): "))
while n5 < 0 or n5 > 10:
    print("Nota inválida. Digite novamente.")
    n5 = float(input("Digite a 5ª nota (0 a 10): "))

menor = min(n1, n2, n3, n4, n5)

soma = n1 + n2 + n3 + n4 + n5
soma = soma - menor
media = soma / 4

print("Menor nota descartada =", menor)
print("Média final =", round(media, 1))