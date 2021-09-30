a, b = input().split()
a = int(a)
b = int(b)

if (b >= 97):
    print("cheia")
else:
    if (b >= 0 and b <= 2):
        print("nova")
    if (b >= 3 and b <= 96 and a < b):
        print("crescente")
    if (b >= 3 and b <= 96 and a > b):
        print("minguante")