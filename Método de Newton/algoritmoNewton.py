#########################################
#  Algoritmo do método de Newton        #
#                                       #
#  Projeto de Cálculo Numérico S4 BCC   #
#                                       #
#  Alisson Chaves Ferreira              #
#                                       #
#                                シ     #   
#########################################

import math
import tkinter as tk

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

def avaliar_expressao():
    fx = (fx_entrada.get()).lower()
    x0 = float(x0_entrada.get())
    precisao = notac_cientif(precisao_entrada.get())
    
    cont = 0
    Ni = 100  #número máximo de iterações
    x1 = x0
    
    resultado_texto.delete(1.0, tk.END)
    resultado_texto.insert(tk.END, '\nIteração  |               x            |          f(x)              |\n')
    resultado_texto.insert(tk.END, '-' * 80 + '\n')

    while True:
        resultado_texto.insert(tk.END, f'   {cont:3d}    |   {x1:12.8f}   |   {funcao(x1, fx):12.8f}\n')
        x1 = x0 - funcao(x0, fx)/derivada(x0, fx)
        x0 = x1
        
        cont += 1
        
        if cont >= Ni or math.fabs(funcao(x0, fx)) < precisao:
            resultado_texto.insert(tk.END, f'   {cont:3d}    |   {x1:12.8f}   |   {funcao(x1, fx):12.8f}')
            break
            
    resultado_texto.insert(tk.END, f'\nRaiz: {x0:.8f}\n')
    resultado_texto.insert(tk.END, f'Iterações: {cont+1}\n')
    resultado_texto.insert(tk.END, f'f({x0:.8f}) = ({funcao(x0, fx):.8f})\n')

def sair(): # função para fechar a janela
    janela.destroy()
    
janela = tk.Tk()

arial = ('Arial', 12)
arial_black = ('Arial Black', 12) # fonte passada no paramêtro font

largura_janela = 500
altura_janela = 400

janela.title("Método do Ponto Fixo")

quadro = tk.Frame(janela)
quadro.pack(padx=20, pady=20)

informacoes = tk.Label(quadro, text=
'''Bem vindo ao algoritmo do Método de Newton!

Aqui você poderá digitar fórmulas de forma contínua!
Você poderá usar: sen ,cos ,tg ,log ,e , exp e raiz usando sqrt.

Exemplo de função para o auxílio no programa:

f(x) = x**3 - 9 + 3   
x0 = 0.5    
Precisão: 0.0001     
----------------------------
f(x) = x**2 + x - 6   
x0 = 1.5    
Precisão: 2 
----------------------------

''', font= 'bolt', foreground='#5e122f')
informacoes.grid(row= 0, rowspan= 20, column= 9, columnspan= 40)

fx_rotulo = tk.Label(quadro, text='Função f(x):', font=arial_black, foreground='red' ) 
fx_rotulo.grid(row=0, column=0, sticky="s")

fx_entrada = tk.Entry(quadro, font=arial_black, foreground='red') # Área onde o usuário digita a f(x)
fx_entrada.grid(row=0, column=1, sticky='w')

x0_rotulo = tk.Label(quadro, text='Valor inicial x0: ', font=arial_black, foreground='blue')
x0_rotulo.grid(row=2, column=0, sticky="s")

x0_entrada = tk.Entry(quadro, font=arial_black, foreground=  'blue') # Área onde o usuário digita o paramêtro final 'b'
x0_entrada.grid(row=2, column=1, sticky='w')

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
