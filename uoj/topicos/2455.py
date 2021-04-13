p1,c1,p2,c2 = input().split()

esquerda = int(p1) * int(c1)
direita = int(p2) * int(c2)

if esquerda == direita:
    print(0)
elif esquerda > direita:
    print(-1)
else:
    print(1)
