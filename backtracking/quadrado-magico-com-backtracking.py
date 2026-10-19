
N = 3 #4
SOMA = 9 #34

quadrado = [[0] * N for _ in range(N)]
usados = set()


def backtracking(pos):
    # Todas as células foram preenchidas
    if pos == N * N:
        return True

    linha = pos // N
    coluna = pos % N

    # Tenta os números de 1 a 9
    for num in range(1, N * N + 1):
        if num in usados:
            continue

        quadrado[linha][coluna] = num
        usados.add(num)

        # Verifica se a configuração parcial é válida
        if valido(linha, coluna):
            if backtracking(pos + 1):
                return True

        # Backtracking: desfaz a escolha
        usados.remove(num)
        quadrado[linha][coluna] = 0

    return False


def valido(linha, coluna):
    # Verifica a linha quando estiver completa
    if coluna == N - 1:
        if sum(quadrado[linha]) != SOMA:
            return False

    # Verifica a coluna quando estiver completa
    if linha == N - 1:
        if sum(quadrado[i][coluna] for i in range(N)) != SOMA:
            return False

    # Diagonal principal
    if linha == coluna and linha == N - 1:
        if sum(quadrado[i][i] for i in range(N)) != SOMA:
            return False

    # Diagonal secundária
    if linha + coluna == N - 1 and linha == N - 1:
        if sum(quadrado[i][N - 1 - i]
               for i in range(N)) != SOMA:
            return False

    return True


if backtracking(0):
    for linha in quadrado:
        print(*linha)
else:
    print("Nenhuma solução encontrada.")
