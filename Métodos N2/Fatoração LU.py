def LU(A):
    n = len(A)

    for k in range(1, n):
        for i in range(k + 1, n + 1):
            m = A[i - 1][k - 1] / A[k - 1][k - 1]
            A[i - 1][k - 1] = m
            for j in range(k + 1, n + 1):
                A[i - 1][j - 1] = A[i - 1][j - 1] - m * A[k - 1][j - 1]

    return A

# Resolve o sistema triangular inferior.
def TriangularInferior(L, b):
    n = len(b)
    y = [0] * n

    for i in range(1, n + 1):
        s = 0
        for j in range(1, i):
            s = s + L[i - 1][j - 1] * y[j - 1]
        y[i - 1] = b[i - 1] - s

    return y

# Resolve o sistema triangular superior.
def TriangularSuperior(U, b):
    n = len(b)
    x = [0] * n
    x[n - 1] = b[n - 1] / U[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += U[i][j] * x[j]
        x[i] = (b[i] - s) / U[i][i]

    return x

def definir_matriz_e_vetor():
    dimensao = int(input('Dimensão da matriz: '))
    matriz_coeficientes = []

    for i in range(dimensao):
        valores = input(f'Valores da linha {i + 1}, separados por espaço: ')
        valores_coeficientes = [float(x) for x in valores.split()]
        matriz_coeficientes.append(valores_coeficientes)

    vetor_termos_independentes = []
    for i in range(dimensao):
        termo = float(input(f'Termo independente da linha {i + 1}: '))
        vetor_termos_independentes.append(termo)

    return matriz_coeficientes, vetor_termos_independentes

# gaulssPivoteamento([[1, 2, -1], [2, -1, 1], [1, 1, 1]], [2, 3, 6])

# Teste com dados inseridos pelo usuário.
matriz_inserida, vetor_inserido = definir_matriz_e_vetor()

# Obtendo os fatores L e U.
A = LU(matriz_inserida)
print(f"\nMatriz LU (A):", f'\033[1;34m{A}\033[m')

y = TriangularInferior(A, vetor_inserido)
print("Solução y:", f'\033[1;32m{y}\033[m')

x = TriangularSuperior(A, y)
print("Solução x:", f'\033[1;32m{x}\033[m')
