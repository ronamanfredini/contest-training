while True:
    h,m,h2,m2 = input().split()
    
    mt1 = int(h) * 60 + int(m)
    mt2 = int(h2) * 60 + int(m2)

    if mt1 > mt2:
        mt2 = mt2 + 1440

    mt = mt2 - mt1
    if mt1 == mt2:
        mt = 1440
     

    if h == '0' and m == '0' and h2 == '0' and m2 == '0':
        break
    
    print(mt)

