import math

# Mapeamento de termos para funções
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

def avaliar_expressao():
    print('Para a função, use valores parecidos com: x**2 - x - 2')

    print('\033[1m1 - Encontrar raiz!\033[m')
    print('\033[1m2 - Sair do programa!\033[m')



    fx = input('Digite a f(x) = ')
    a = float(input('Digite o valor do intervalo "a" no intervalo: '))
    b = float(input('Digite o valor do intervalo "b" no intervalo: '))
    precisao = float(input('Digite a precisão do algoritmo: ')) # precisão desejada para a solução


    amplitude = b - a

    x0 = (a*funcao(b, fx) - b*funcao(a, fx))/(funcao(b, fx) - funcao(a, fx)) #sequência de aproximações, divisão do intervalo

    cont = 0
    Ni = 100 #numero de iterações, para evitar um possível loop infinito


    print('\nIteração  |         x        |        f(x)      |     b - a')
    print('-' * 64)

    while math.fabs(funcao(x0, fx)) > precisao: #calculo valor absoluto da função em modulo
        
        x0 = (a*funcao(b, fx) - b*funcao(a, fx))/(funcao(b, fx) - funcao(a, fx)) #calculo de nova aproximação
        if funcao(a, fx) * funcao(x0, fx) < 0:
            b = x0
        if funcao(a, fx) * funcao(x0, fx) > 0:
            a = x0
            
        amplitude = b - a
        cont = cont + 1
        if cont >= Ni:
            break
        
        print(f'   {cont:3d}    |   {x0:12.8f}   |   {funcao(x0, fx):12.8f}   |   {amplitude:10.8f}')
        
        
        
    print(f'Raiz: {x0:.8f}')
    print('Iterações: ', cont)
    print(f'f({x0:.8f}) = ({funcao(x0, fx):.8f})')


    # não foi feito o uso do  or "math.fabs(funcao(x0, fx)) > precisao" por conta da quantidade de iterações em algumas funções
    # alcansarem valores infinitos
