
while True:
    casos = int(input())
    if casos == 0:
        break

    sinais = [int(x) for x in input().split()]
    sinais.append(sinais[0])
    sinais.append(sinais[1])
    pico_count = 0

    for i in range(1, casos + 1):
        if sinais[i] < sinais[i - 1] and sinais[i] < sinais[i + 1]:
            pico_count += 1

        elif sinais[i] > sinais[i - 1] and sinais[i] > sinais[i + 1]:
            pico_count += 1
    print(pico_count)

