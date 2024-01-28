import math

def eliminacao_gaussiana_sem_Pivoteamento(matriz_coeficientes, termo_independente):
    n = len(matriz_coeficientes)

    for i in range(n):
        for j in range(i+1, n):
            multiplicador = matriz_coeficientes[j][i] / matriz_coeficientes[i][i]
            for k in range(i, n):
                matriz_coeficientes[j][k] -= multiplicador * matriz_coeficientes[i][k]
            termo_independente[j] -= multiplicador * termo_independente[i]

    
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = termo_independente[i]
        for j in range(i + 1, n):
            x[i] -= matriz_coeficientes[i][j] * x[j]
        x[i] /= matriz_coeficientes[i][i]
        
    # Printar resultados
    print("\nMatriz Resultante:")
    for i in range(len(matriz_coeficientes)):
        for j in range(len(matriz_coeficientes)):
            print(f'\033[1;33m{matriz_coeficientes[i][j]:>4}\033[m ', end='')
        print(f'| \033[1;36m{termo_independente[i]:<5}\033[m')

    print('\nSolução de X:')
    for i, valor_x in enumerate(x):
        print(f'x\033[1;30m{i + 1}\033[m = \033[1;32m{valor_x}\033[m')

    return x

dimensao = int(input('Dimensão da matriz: '))

def definir_matriz():

    matriz_coeficientes = []

    for i in range(dimensao):
        valores = input(f'Valores da linha {i + 1}, separados por espaço: ')
        valores_coeficientes = [float(x) for x in valores.split()]
        matriz_coeficientes.append(valores_coeficientes)

    return matriz_coeficientes

def ti():
    vetor_ti = []

    for i in range(dimensao):
        termo = float(input(f'Termo independente da linha {i + 1}: '))
        vetor_ti.append(termo)

    return vetor_ti

def imprimir_matriz_e_vetor(matriz, vetor):
    for i in range(dimensao):
        for j in range(dimensao):
            print(f'\033[1;33m{matriz[i][j]:>4}\033[m ', end='')
        print(f'| \033[1;36m{vetor[i]:<5}\033[m')

matriz_inserida = definir_matriz()  
vetor_inserido = ti()

print('\nMatriz digitada:')
imprimir_matriz_e_vetor(matriz_inserida, vetor_inserido)
eliminacao_gaussiana_sem_Pivoteamento(matriz_inserida, vetor_inserido)  