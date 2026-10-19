
from itertools import permutations

N = 3 #4
SOMA = 15 #34

for p in permutations(range(1, N * N + 1)):

    # Verifica as linhas
    if any(
        sum(p[i * N:(i + 1) * N]) != SOMA
        for i in range(N)
    ):
        continue

    # Verifica as colunas
    if any(
        sum(p[i::N]) != SOMA
        for i in range(N)
    ):
        continue

    # Verifica a diagonal principal
    if sum(p[i * N + i] for i in range(N)) != SOMA:
        continue

    # Verifica a diagonal secundária
    if sum(p[i * N + (N - 1 - i)]
           for i in range(N)) != SOMA:
        continue

    # Exibe a primeira solução encontrada
    for i in range(0, N * N, N):
        print(*p[i:i + N])

    break
