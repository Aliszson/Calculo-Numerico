import math

def funcao(x, expressao):
    termos = ['sen', 'cos', 'tg', 'log', 'exp', 'sqrt', 'e']

    for termo in termos:
        if termo in expressao:
            if termo == 'sen':
                expressao = expressao.replace(f'{termo}(', f'math.sin(')
            elif termo == 'tg':
                expressao = expressao.replace(f'{termo}(', f'math.tan(')
            elif termo == 'e':
                expressao = expressao.replace(f'{termo}', f'math.{termo}')
            else:
                expressao = expressao.replace(f'{termo}(', f'math.{termo}(')

    return eval(expressao)
    
def notac_cientif(valor):
    return eval(valor)

print('Para a função, use valores parecidos com: x**2 - x - 2')

x = []
fx = input('Digite a f(x) = ').lower()
x0 = float((input('Valor de x0:')))
x1 = float(input('Valor de x1:'))
precisao = notac_cientif(input('Digite a precisão do algoritmo: '))

x.append(x0)
x.append(x1)

cont = 0
Ni = 100  #número máximo de iterações
n = 1
xn = x1

print('\nIteração  |         x        |        f(x)      ')
print('-' * 48)

while True:
    
    print(f'   {cont:3d}    |   {xn:12.8f}   |   {funcao(xn, fx):12.8f}')
    xn = x[n] - (x[n] - x[n-1])/(funcao(x[n], fx) - funcao(x[n-1], fx))*funcao(x[n], fx)
    x.append(xn)
    n+=1
    cont += 1
    if cont >= Ni or math.fabs(funcao(xn, fx)) < precisao:
        print(f'   {cont:3d}    |   {xn:12.8f}   |   {funcao(xn, fx):12.8f}')
        break
            
print(f'Raiz: {xn:.8f}')
print('Iterações: ', cont)
print(f'f({xn:.8f}) = ({funcao(xn, fx):.8f})')