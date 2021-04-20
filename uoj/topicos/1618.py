n = input()

for i in range(int(n)):
    firstX, firstY, secondX, secondY, thirdX, thirdY, fourthX, fourthY, fifthX, fifthY = input().split(' ')
    firstX = int(firstX)
    firstY = int(firstY)
    secondX = int(secondX)
    secondY = int(secondY)
    thirdX = int(thirdX)
    thirdY = int(thirdY)
    fourthX = int(fourthX)
    fourthY = int(fourthY)
    fifthX = int(fifthX)
    fifthY = int(fifthY)
    if fifthX >= firstX and fifthX <= secondX and fifthX >= fourthX and fifthX <= thirdX and fifthY >= firstY and fifthY <= fourthY and fifthY >= secondY and fifthY <= thirdY:
        print("1")
    else:
        print("0")