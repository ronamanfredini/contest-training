quantidade_retangulos = [1, 2, 4, 8, 16, 32, 64, 128, 256]
meu_numero_da_chamada = 20
pt = meu_numero_da_chamada * 4

for i in quantidade_retangulos:
    deltaX = 3 / i
    area = 0
    for j in range(1, i):
        c = (j - 1 + pt / 100) * deltaX
        f = 3 - (1 / 3) * pow(c, 2)
        area += f * deltaX
    print("Área calculada " + str(i) + " = " + str(area))
    a = 6 + 9 / (2 * i) - 3 / (2 * pow(i,2)) + (9 * pt * (1/10000)) * (-100 + 100 / i - pt/i) / i
    print("Prova real " + str(i) + " = " + str(a))

