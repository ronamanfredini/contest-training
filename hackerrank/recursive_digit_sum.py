def doSum(n):
	if (len(n) <= 1): return n

	result = 0
	for i in n:
		result += int(i)

	return doSum(str(result))


def superDigit(n, k):
	numStr = ''
	for i in range(0, k):
		numStr += str(n)
	return doSum(numStr)


print(superDigit(148,3))