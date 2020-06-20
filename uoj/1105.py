g = input()

while (g != '0 0'):
	bankReserves = input()
	bankReserves = bankReserves.split(' ')

	for i in range(0, len(bankReserves)):
		bankReserves[i] = int(bankReserves[i])
		
	transactionCount = int(g.split(' ')[1])
	consistent = True
	for i in range(0, transactionCount):
		transactionDefinition = input()
		if (consistent):
			transactionDefinition = transactionDefinition.split(' ')
			debtor = int(transactionDefinition[0])
			creditor = int(transactionDefinition[1])
			amount = int(transactionDefinition[2])

			if (bankReserves[debtor - 1] < amount):
				consistent = False
				continue

			bankReserves[debtor - 1] -= amount
			bankReserves[creditor - 1] += amount
		
	if (consistent):
		print('S')
	else:
		print('N')


	g = input()
