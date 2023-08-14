import math

def f(x): # função própia para definicão do f(x)
    return(x**2 - x - 2)

a = float(input('Digite o valor do intervalo "a" no intervalo: '))
b = float(input('Digite o valor do intervalo "b" no intervalo: '))

precisao = 0.001 # precisão desejada para a solução

tolerancia = 0.0001 

amplitude = b - a

x0 = (a + b)/2.0 #sequência de aproximações, divisão do intervalo em duas sessões (bisseção)

cont = 0
Ni = 100 #numero de iterações


print('\nIteração  |         x        |        f(x)      |     b - a')
print('-' * 64)

while (amplitude > precisao or math.fabs(f(x0)) > tolerancia): #calculo valor absoluto da função em modulo
    if f(a) * f(x0) < 0:
        b = x0
    if f(a) * f(x0) > 0:
        a = x0
    
    amplitude = b - a
    x0 = (a + b)/2 #calculo de nova aproximação
    cont = cont + 1
    if cont >= Ni:
        break
    
    print(f'   {cont:3d}    |   {x0:12.8f}   |   {f(x0):12.8f}   |   {amplitude:10.8f}')
    
    
    
print(f'Raiz: {x0:.8f}')
print('Iterações: ', cont)
print(f'f({x0:.8f}) = ({f(x0):.8f})')
