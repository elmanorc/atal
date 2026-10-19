notas = [100, 50, 20, 10, 5, 2, 1]
valor = int(input())

print(valor)
for i in range(len(notas)):
    q = valor // notas[i]
    valor -= q * notas[i]
    print(q, "nota(s) de R$", notas[i], ",00")