def isDiagonal(damaX, damaY, targetX, targetY):
	if (abs(damaY - damaX) == abs(targetPosY - targetX)):
		return True
	exp = (targetX == targetY + damaY - damaX or targetY ==  - targetX + damaY + damaX)
	if (abs(exp) == 1):
		return True
	return False

lines = input()

while True:
	numbers = lines.split(' ')

	damaPosX = int(numbers[0])
	damaPosY = int(numbers[1])
	if (damaPosX == 0):
		break

	targetPosX = int(numbers[2])
	targetPosY = int(numbers[3])

	if (damaPosX == targetPosX and damaPosY == targetPosY):
		print(0)
	elif ((damaPosX == targetPosX and damaPosY != targetPosY) or (damaPosY == targetPosY and damaPosX != targetPosX)):
		print(1)
	elif (isDiagonal(damaPosX, damaPosY, targetPosX, targetPosY)):
		print(1)
	else:
		print(2)

	lines = input()