import matplotlib.pyplot as plt
import numpy as np

# Exemplo de plotagem com notação matemática LaTeX
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.title(r'Gráfico da função $y = \sin(x)$')
plt.show()
