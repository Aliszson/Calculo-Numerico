import math
import tkinter as tk
from tkinter import messagebox

def f(x):
    return x**2 - x - 2.0

def calcular_raiz():
    a = float(entry_a.get())
    b = float(entry_b.get())
    precisao = float(entry_precisao.get())
    tolerancia = float(entry_tolerancia.get())

    amplitude = b - a
    x0 = (a + b) / 2.0
    cont = 0
    Ni = 100

    try:
        while amplitude > precisao or math.fabs(f(x0)) > tolerancia:
            if f(a) * f(x0) < 0.0:
                b = x0
            if f(a) * f(x0) > 0.0:
                a = x0

            amplitude = b - a
            x0 = (a + b) / 2.0
            cont = cont + 1
            if cont >= Ni:
                break

        resultado_label.config(text=f'Raiz: {x0:.8f}\nIterações: {cont}\nf({x0:.8f}) = {f(x0):.8f}')
    except Exception as e:
        resultado_label.config(text=f"Erro: {e}")

# Criar janela
root = tk.Tk()
root.geometry('300x300')
root.title("Método da Bissecção")

# Criar widgets
tk.Label(root, text="Intervalo [a; b]").pack()
entry_a = tk.Entry(root)
entry_a.pack()
entry_b = tk.Entry(root)
entry_b.pack()

tk.Label(root, text="Precisão desejada").pack()
entry_precisao = tk.Entry(root)
entry_precisao.pack()

tk.Label(root, text="Tolerância").pack()
entry_tolerancia = tk.Entry(root)
entry_tolerancia.pack()

calcular_button = tk.Button(root, text="Calcular Raiz", command=calcular_raiz)
calcular_button.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

# Iniciar loop da interface gráfica
root.mainloop()
