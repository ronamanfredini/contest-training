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
    print(area)
    
