while True:
    try:

        a,b,c = input().split()
        
        is_c = a == '1' and b == '1' and c == '0' or a == '0' and b == '0' and c == '1'
        is_b = a == '1' and c == '1' and b == '0' or a == '0' and c == '0' and b == '1'
        is_a = b == '1' and c == '1' and a == '0' or b == '0' and c == '0' and a == '1'
        
        if is_c:
            print('C')
        elif is_b:
            print('B')
        elif is_a:
            print('A')
        else:
            print('*')
    
    except:
        break
