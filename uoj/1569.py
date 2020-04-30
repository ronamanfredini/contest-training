cases = int(input())

tabletop = []
for i in range(0, 99):
				# posição, escada, escorregador
	positionDef = [i + 1, False, False]
	tabletop.append(positionDef)

for i in range(0, cases - 1):
	definitions = input()
	definitions = definitions.split(' ')
	playersCount = int(definitions[0])
	laddersAndSlidersCount = int(definitions[1])
	diceRolls = int(definitions[2])

	for j in range(0, laddersAndSlidersCount - 1):
		initialAndEndPosition = input()
		initialAndEndPosition = initialAndEndPosition.split(' ')
		initialPosition = int(initialAndEndPosition[0])
		endPosition = int(initialAndEndPosition[1])

		