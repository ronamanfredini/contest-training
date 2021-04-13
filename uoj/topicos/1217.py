sf, sn, totkg = 0, 0, 0
n = int(input())
for i in range(n):
    sf += float(input())
    l = len(input().split())
    sn += 1
    totkg += l
    print("day {}: {} kg".format(i+1, l))
print("{:.2f} kg by day\nR$ {:.2f} by day".format(totkg/sn, sf/n))