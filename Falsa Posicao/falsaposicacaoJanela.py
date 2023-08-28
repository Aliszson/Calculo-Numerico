#########################################
#  Algoritmo do método da Falsa Posição #
#                                       #
#  Projeto de Cálculo Numérico S4 BCC   #
#                                       #
#  Alisson Chaves Ferreira              #
#                                       #
#                                シ     #   
#########################################

import math
import tkinter as tk
from tkinter import messagebox  

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



    fx = fx_entrada.get()
    a = float(a_entrada.get())
    b = float(b_entrada.get())
    precisao = float(precisao_entrada.get())  # precisão desejada para a solução


    amplitude = b - a

    x0 = (a*funcao(b, fx) - b*funcao(a, fx))/(funcao(b, fx) - funcao(a, fx)) #sequência de aproximações, divisão do intervalo

    cont = 0
    Ni = 100 #numero de iterações, para evitar um possível loop infinito

    resultado_texto.delete(1.0, tk.END)
    resultado_texto.insert(tk.END, '\nIteração  |            x          |             f(x)            |        b - a\n')
    resultado_texto.insert(tk.END, '-' * 105 + '\n')

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
        
        resultado_texto.insert(tk.END, f'   {cont:3d}    |    {x0:12.8f}   |     {funcao(x0, fx):12.8f}     |      {amplitude:10.8f}\n')
        
    resultado_texto.insert(tk.END, f'\nRaiz: {x0:.8f}\n')
    resultado_texto.insert(tk.END, f'Iterações: {cont}\n')
    resultado_texto.insert(tk.END, f'f({x0:.8f}) = ({funcao(x0, fx):.8f})\n')

# Função para análise de inserções de métodos matemáticos variados, fazendo assim seu calculo usando a biclioteca math
# e calculando seu resultado e logo em seguida enviando para a função 'eval' que irá realizar o restante dos cálculos



def sair(): # função para fechar a janela
    janela.destroy()
    
janela = tk.Tk()

arial = ('Arial', 12)
arial_black = ('Arial Black', 12) # fonte passada no paramêtro font

largura_janela = 500
altura_janela = 400

janela.title("Método da Falsa Posição")

quadro = tk.Frame(janela)
quadro.pack(padx=20, pady=20)

informacoes = tk.Label(quadro, text=
'''Bem vindo ao algoritmo de método da Falsa Posição!

Aqui você poderá digitar fórmulas de forma contínua!
Você poderá usar: sen ,cos ,tg ,log ,e , exp e raiz usando sqrt.

Alguns exemplos de funções para o auxílio no programa:

f(x) = x**3 + sen(3)   
Intervalo: -5 e 5      
Precisão: 0.0001      
----------------------------
f(x) = tg(x) - 2**x 
Intervalo: -2 a 1
Precisão: 0.0001
----------------------------
f(x) = sen(x) - cos(x)
Intervalo: - 1 e 1
Precisão: 0.0001
----------------------------
f(x) = sqrt(x) - 2
Intervalo: 0 e 5
Precisão: 0.000001

''', font= 'bolt', foreground='#5e122f')
informacoes.grid(row= 0, rowspan= 20, column= 9, columnspan= 40)

fx_rotulo = tk.Label(quadro, text="Função f(x):", font=arial_black, foreground='red' ) 
fx_rotulo.grid(row=0, column=0, sticky="s")

fx_entrada = tk.Entry(quadro, font=arial_black, foreground='red') # Área onde o usuário digita a f(x)
fx_entrada.grid(row=0, column=1, sticky='w')

a_rotulo = tk.Label(quadro, text="Valor do intervalo a:", font=arial_black, foreground='blue')
a_rotulo.grid(row=1, column=0, sticky="s")

a_entrada = tk.Entry(quadro, font=arial_black, foreground='blue') # Área onde o usuário digita o paramêtro inicial 'a'
a_entrada.grid(row=1, column=1, sticky='w')

b_rotulo = tk.Label(quadro, text="Valor do intervalo b:", font=arial_black, foreground='blue')
b_rotulo.grid(row=2, column=0, sticky="s")

b_entrada = tk.Entry(quadro, font=arial_black, foreground=  'blue') # Área onde o usuário digita o paramêtro final 'b'
b_entrada.grid(row=2, column=1, sticky='w')

precisao_rotulo = tk.Label(quadro, text="Precisão:", font=arial_black, foreground='orange')
precisao_rotulo.grid(row=3, column=0, sticky="s")

precisao_entrada = tk.Entry(quadro, font=arial_black, foreground='orange') # Área onde o usuário digita a precisão do algoritmo
precisao_entrada.grid(row=3, column=1, sticky='w')

calcular_botao = tk.Button(quadro, text="Calcular", command=avaliar_expressao, font=arial_black, foreground='yellow', background='green', borderwidth= 8, relief="groove")
calcular_botao.grid(row=4, columnspan=2, pady=10)

resultado_texto = tk.Text(quadro, height=20, width=70, font= arial_black, foreground='orange')
resultado_texto.grid(row=5, columnspan=2)

sair_botao = tk.Button(quadro, text="Sair", command= sair,font= arial_black, foreground='yellow', background='red', borderwidth= 8, relief="groove")
sair_botao.grid(row=6, columnspan=2, pady=10)

janela.mainloop()