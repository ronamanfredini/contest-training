n = int(input())

dicio = [0] * 2001


for i in range(n):
    value = int(input())
    
    dicio[value] = dicio[value] + 1


for i in range(2001):
    if(dicio[i] != 0):
        print(i, 'aparece', dicio[i], 'vez(es)')

