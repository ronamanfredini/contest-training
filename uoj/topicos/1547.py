n = int(input())
for i in range(n):
    qt, s = input().split()
    qt, s = int(qt), int(s)
    contador = 1
    ganhador = 0
    numeros = []
    aux = 0

    resposta = input().split(' ')
    for x in resposta:
        x = int(x)
        tmp = s - x
        if tmp == 0:
            ganhador = contador
            break
        else:
            contador += 1
            if tmp < 0:
                tmp = abs(tmp)
            numeros.append(tmp)
    
    if ganhador == 0:
        contador = 1
        aux = min(numeros)
        for j in numeros:
            j = int(j)
            aux = int(aux)
            if j == aux:
                ganhador = contador
                break
            else:
                contador += 1
    print(ganhador)