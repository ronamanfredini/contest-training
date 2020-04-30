tabletop = {}
for i in range(1, 100):
    tabletop[i] = {'specials': -1}
cases = int(input())

for caseRange in range(0, cases):
    definitions = input()
    definitions = definitions.split(' ')

    playersCount = int(definitions[0])
    players = [1] * playersCount

    laddersAndSlidersCount = int(definitions[1])
    diceRolls = int(definitions[2])

    for i in range(0, laddersAndSlidersCount):
        specialCoordinates = input()
        specialCoordinates = specialCoordinates.split(' ')
        tabletop[int(specialCoordinates[0])]['specials'] = int(specialCoordinates[1])
    
    playerIndexPointer = 0
    for i in range(0, diceRolls):
        roll = int(input())
        players[playerIndexPointer] += roll
        
        while (tabletop[players[playerIndexPointer]]['specials'] != -1):
            players[playerIndexPointer] = tabletop[players[playerIndexPointer]]['specials']
        if (players[playerIndexPointer] == 100):
            break

        playerIndexPointer += 1
        if (playerIndexPointer >= playersCount):
            playerIndexPointer = 0

    for i in range(0, playersCount):
        print("Position of player " + str(i + 1) + " is " + str(players[i]) + '.')


