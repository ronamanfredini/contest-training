while True:
    equacao = input()
    a = equacao.split('+')[0]
    b = equacao.split('+')[1].split('=')[0]
    c = equacao.split('+')[1].split('=')[1]
    
    a_invertido = ''
    b_invertido = ''
    c_invertido = ''

    for i in range(len(a) - 1,-1, -1):
        a_invertido += a[i]
    
    for i in range(len(b) - 1,-1, -1):
        b_invertido += b[i]    
    
    for i in range(len(c) - 1,-1, -1):
        c_invertido += c[i]    

    if int(a_invertido) + int(b_invertido) == int(c_invertido):
        print('True')
    else:
        print('False')

    if a == '0' and b == '0' and c == '0':
        break
    

