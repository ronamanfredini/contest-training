numPecas = int(input())
lavMin, lavMax = input().split(" ")
lavMin = int(lavMin)
lavMax = int(lavMax)
secMin, secMax = input().split(" ")
secMin = int(secMin)
secMax = int(secMax)

if (numPecas >= lavMin and numPecas >= secMin and numPecas <= lavMax and numPecas <= secMax):
    print("possivel")
else:
    print("impossivel")