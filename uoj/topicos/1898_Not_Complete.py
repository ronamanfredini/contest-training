def numChar(num):
    numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    if num not in numbers:
        return False
    return True

def casasDecimais(num, precisao):
    casas = 10**precisao
    return num * casas / casas


linha1 = input().encode('utf-8').strip()
linha2 = input().encode('utf-8').strip()

cpf = ''
cValorFinaldeLinha1 = ''
cValordaLinha2 = ''
limite = 0
limiteponto = 0

ehControledePonto = False
ehpontounico = True


for i in range(len(linha1)):
    if(numChar(linha1[i])):
        if(limite < 11):
            cpf += linha1[i]
            limite += 1
        else:
            if(int(limiteponto) < 2):
                cValorFinaldeLinha1 += linha1[i]

            if(ehControledePonto):
                limiteponto += 1

    elif(linha1[i] == '.' ):
        if(ehpontounico):
            cValorFinaldeLinha1 += '.'
            ehpontounico = False

        ehControledePonto = True

limiteponto = 0
ehControledePonto = False
ehpontounico = True

for j in range(len(linha2)):
    if(numChar(linha2[j])):
        
        cValordaLinha2 += linha2[j]

        if(ehControledePonto):
            if(limiteponto < 1 ):
                limiteponto += 1
            else:
                break
        
    elif ( linha2[j] == '.'):
        if(ehpontounico):
            cValordaLinha2 += '.'
            ehpontounico = False
        ehControledePonto = True

print("cValorFinaldeLinha1", cValorFinaldeLinha1)
resultado1 = float(cValorFinaldeLinha1)
resultado2 = float(cValordaLinha2)
resultadoPreciso1 = casasDecimais(resultado1, 2)
resultadoPreciso2 = casasDecimais(resultado2, 2)
resultado = resultadoPreciso1 + resultadoPreciso2
print("cpf", cpf)
print(round(resultado,2))
