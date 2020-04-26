winesBank = []
operationsSum = 0
winesBankPolarity = ''

def subtractFromWinesBank(quantity, houseIndex):
    global winesBank, operationsSum, winesBankPolarity
    winesBankLastItem = winesBank[len(winesBank) - 1]
    diff = abs(winesBankLastItem[0]) - abs(quantity)
    
    multiplier = houseIndex - winesBankLastItem[1]
    if (diff == 0):
        operationsSum += abs(quantity) * multiplier
        winesBank.pop(len(winesBank) - 1)
    if (diff > 0):
        winesBank[len(winesBank) - 1][0] = diff
        operationsSum += abs(quantity) * multiplier
    if (diff < 0):
        operationsSum += abs(winesBankLastItem[0]) * multiplier
        winesBank.pop(len(winesBank) - 1)
        if (len(winesBank) > 0):
            subtractFromWinesBank(diff, houseIndex)
        else:
            winesBank.append([diff, houseIndex])
            if (winesBankPolarity == '+'):
                winesBankPolarity = '-'
            else:
                winesBankPolarity = '+'


inputCases = int(input())

while (inputCases != 0):
    operationsSum = 0
    winesBank = []
    winesBankPolarity = ''
    houseWines = input()
    houseWines = houseWines.split(' ')

    for i in range(0, len(houseWines)):
        winesNeeded = int(houseWines[i])
        if (len(winesBank) == 0):
            winesBank.append([winesNeeded, i])
            if (winesNeeded > 0):
                winesBankPolarity = '+'
            else:
                winesBankPolarity = '-'
            continue

        if ((winesNeeded > 0 and winesBankPolarity == '+') or (winesNeeded < 0 and winesBankPolarity == '-')):
            winesBank.append([winesNeeded, i])
            continue

        subtractFromWinesBank(winesNeeded, i)

                        
    print (operationsSum)
    
    inputCases = int(input())