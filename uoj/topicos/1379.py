while True:
    a,b = input().split()
    
    c = 2 * int(a) - int(b)

    if a == '0' and b == '0':
        break
    
    print(c)
