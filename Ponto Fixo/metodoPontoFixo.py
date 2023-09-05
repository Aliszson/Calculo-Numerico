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

fx = input('Digite a f(x) = ').lower()
iter_func = input('Digite a função de iteração phi(x): ').lower()
x0 = float(input('Digite o valor inicial x0: ')) 
precisao = notac_cientif(input('Digite a precisão do algoritmo: '))

cont = 0
Ni = 100  #número máximo de iterações

print('\nIteração  |         x        |        f(x)      ')
print('-' * 48)

while True:
    x1 = funcao(x0, iter_func)
    
    amplitude = math.fabs(x1 - x0)
    cont += 1
    
    print(f'   {cont:3d}    |   {x1:12.8f}   |   {funcao(x1, fx):12.8f}')
    if cont >= Ni or amplitude < precisao:
        break
    x0 = x1
    
print(f'Raiz: {x1:.8f}')
print('Iterações: ', cont)
print(f'f({x1:.8f}) = ({funcao(x1, fx):.8f})')