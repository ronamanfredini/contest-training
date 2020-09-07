from sympy import *

init_printing()
var('x,y')

intervalo = [1.0, 1.5]
resultado_final = 1.1161
e = 10 ** -2
f_de_x = Lambda(x, (2 * x ** 3 + log(x ** 2) - 3))

derivada = diff(f_de_x(x), x)

x_n = intervalo[0]
iteracao = 0

while(x_n <= intervalo[1] and iteracao < 8):
    der_uma_linha = derivada.subs(x, x_n)
    f = f_de_x(x_n)
    teste_conv = f * diff(derivada, x).subs(x, x_n)

    if(teste_conv > 0): 
        x_n_aux = x_n
        x_n = x_n - (f / der_uma_linha)
        string_saida = 'n= {0}, Xn={1}, f(Xn) = {2}, e < {3} = {4}'
        print(string_saida.format(iteracao, f, x_n, e, x_n_aux - x_n))
        print(teste_conv)

        if(x_n_aux - x_n == 0):
            break
        iteracao = iteracao + 1
    else:
        x_n = intervalo[1]
