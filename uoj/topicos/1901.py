tam_floresta = int(input())

matriz=[]

for i in range(0, tam_floresta):
    linhas = input().split()
    matriz.append(linhas)

visitadas = list()
for i in range(0, tam_floresta * 2):
    linha, coluna = input().split()
    linha = int(linha) - 1
    coluna = int(coluna) - 1
    
    borboleta = matriz[linha][coluna]
    if borboleta not in visitadas:
        visitadas.append(borboleta)

print(len(visitadas))

    
