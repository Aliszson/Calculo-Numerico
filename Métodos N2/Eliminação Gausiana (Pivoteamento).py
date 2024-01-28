import math

def solucao(A, b):
    vetorSolucao = []
    for i in range(len(A)):
        vetorSolucao.append(0)
    linha = len(A) - 1
    while linha >= 0:
        x = b[linha]
        coluna = len(A) - 1
        while coluna > linha:
            x-=A[linha][coluna]*vetorSolucao[coluna]
            coluna -= 1
        x/= A[linha][linha]
        linha -= 1
        vetorSolucao[coluna] = x

    for j in range(len(vetorSolucao)):
        print(f'x\033[1;30m{str(j+1)}\033[m = \033[1;32m{str(vetorSolucao[j])}\033[m')

# A: Matriz dos coeficientes
# b: vetor coluna dos termos independentes
def gaussPivoteamento(A, b):
    # acessando as linhas
    for i in range(len(A)):
        # verificando o maior pivô
        pivo = math.fabs(A[i][i])
        linha_pivo = i
        
        for j in range(i+1, len(A)):
            if math.fabs(A[j][i]) > pivo:
                pivo = math.fabs(A[j][i])
                linha_pivo = j
                
        # permutar linhas (caso necessário)
        if linha_pivo != i:
            linha_auxiliar = A[i]
            A[i] = A[linha_pivo]
            A[linha_pivo] = linha_auxiliar
            
            b_auxiliar = b[i]
            b[i] = b[linha_pivo]
            b[linha_pivo] = b_auxiliar
        
        # eliminação gaussiana
        for m in range(i+1, len(A)):
            multiplicador = A[m][i]/A[i][i]
            for n in range(i, len(A)):
                A[m][n] -= multiplicador*A[i][n]
            b[m] -= multiplicador*b[i] 
                    
    # printar matriz A escalonada e vetor b escalonado
    print("\nMatriz resultante:")
    for i in range(len(A)):
        for j in range(len(A)):
            print(f'\033[1;33m{A[i][j]:>4}\033[m ', end='')
        print(f'| \033[1;36m{b[i]:<5}\033[m')

    print("\nResultados: ")
    solucao(A,b)
# gaussPivoteamento([[1, 2, -1], [2, -1, 1], [1, 1, 1]], [2, 3, 6])

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

matriz_inserida = definir_matriz()
vetor_inserido = ti()

def imprimir_matriz_e_vetor(matriz, vetor):
    for i in range(dimensao):
        for j in range(dimensao):
            print(f'\033[1;33m{matriz[i][j]:>4}\033[m ', end='')
        print(f'| \033[1;36m{vetor[i]:<5}\033[m')
        
print('\nMatriz digitada:')
imprimir_matriz_e_vetor(matriz_inserida, vetor_inserido)
gaussPivoteamento(matriz_inserida, vetor_inserido)
