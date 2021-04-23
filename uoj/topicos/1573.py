while True:
    a,b,c = map(int, input().split())

    v = a * b * c

    aresta = v ** (1/3)

    if a == 0 and b == 0 and c == 0 :
        break
    
    print(str(int(aresta)))

