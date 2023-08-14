import math
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def funcao(x, func):
    return eval(func)

def calcular_raiz():
    fu = entry_funcao.get()
    a = float(entry_a.get())
    b = float(entry_b.get())
    precisao = float(entry_precisao.get())
    tolerancia = 0.0001

    amplitude = b - a
    x0 = (a + b) / 2.0
    cont = 0
    Ni = 100

    try:
        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete('1.0', tk.END)
        resultado_text.insert(tk.END, '\nIteração  |         x        |        f(x)      |     b - a\n' + '-' * 64)
        while (amplitude > precisao or math.fabs(funcao(x0, fu)) > tolerancia):
            if funcao(a, fu) * funcao(x0, fu) < 0:
                b = x0
            if funcao(a, fu) * funcao(x0, fu) > 0:
                a = x0
            
            amplitude = b - a
            x0 = (a + b) / 2
            cont = cont + 1
            if cont >= Ni:
                break
            
            resultado_text.insert(tk.END, f'\n   {cont:3d}    |   {x0:12.8f}   |   {funcao(x0, fu):12.8f}   |   {amplitude:10.8f}')
            
        resultado_text.insert(tk.END, f'\n\nRaiz: {x0:.8f}\nIterações: {cont}\nf({x0:.8f}) = ({funcao(x0, fu):.8f})')
        resultado_text.config(state=tk.DISABLED)
    except Exception as e:
        resultado_text.config(state=tk.NORMAL)
        resultado_text.delete('1.0', tk.END)
        resultado_text.insert(tk.END, f"Erro: {e}")
        resultado_text.config(state=tk.DISABLED)

# Criar janela
root = tk.Tk()
root.title("Método da Bissecção")
root.configure(bg='lightgray')

# Carregar imagem de fundo
bg_image = Image.open("455565.png")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Criar widgets
tk.Label(root, text="Função (use 'x' como variável)", bg='lightgray').pack()
entry_funcao = tk.Entry(root)
entry_funcao.pack()

tk.Label(root, text="Intervalo [a; b]", bg='lightgray').pack()
entry_a = tk.Entry(root)
entry_a.pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Precisão desejada", bg='lightgray').pack()
entry_precisao = tk.Entry(root)
entry_precisao.pack()

calcular_button = tk.Button(root, text="Calcular Raiz", command=calcular_raiz, bg='gray', fg='white')
calcular_button.pack()

resultado_text = tk.Text(root, height=15, width=60, bg='white', state=tk.DISABLED)
resultado_text.pack()

# Iniciar loop da interface gráfica
root.mainloop()
