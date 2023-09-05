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

def derivada(x, fx):
    h = 0.00000001
    return((funcao(x + h, fx) - funcao(x, fx))/h)
    
def notac_cientif(valor):
    return eval(valor)

print('Para a função, use valores parecidos com: x**2 - x - 2')

fx = input('Digite a f(x) = ').lower()
x0 = float(input('Digite a aproximação x0: ')) 
precisao = notac_cientif(input('Digite a precisão do algoritmo: '))

cont = 0
Ni = 100  #número máximo de iterações
x1 = x0

print('\nIteração  |         x        |        f(x)      ')
print('-' * 48)

while True:  
    print(f'   {cont:3d}    |   {x1:12.8f}   |   {funcao(x1, fx):12.8f}')
    
    x1 = x0 - funcao(x0, fx)/derivada(x0, fx)
    x0 = x1
    
    cont += 1
    
    if cont >= Ni or math.fabs(funcao(x0, fx)) < precisao:
        print(f'   {cont:3d}    |   {x1:12.8f}   |   {funcao(x1, fx):12.8f}')
        break
               
print(f'Raiz: {x1:.8f}')
print('Iterações: ', cont+1)
print(f'f({x1:.8f}) = ({funcao(x1, fx):.8f})')