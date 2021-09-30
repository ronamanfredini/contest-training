n = int(input())
tempo_padrao = 10

while(n != 0):
    tempo = 10
    if(n < 2):
        pessoas = input().split(" ")
        tempo = tempo_padrao
    else:        
        pessoas = input().split(" ")
        for i in range(0,len(pessoas)-1):
            tempo_entre_pessoas = int(pessoas[i+1]) - int(pessoas[i])
            if(tempo_entre_pessoas > 10):
                tempo = tempo + 10
            else:
                tempo = tempo + tempo_entre_pessoas
    print(tempo)

    n = int(input())
