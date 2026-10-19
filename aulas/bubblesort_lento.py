import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Criar um array já ordenado com 1 milhão de números
array = list(range(100000))

# Marcar o tempo antes da ordenação
inicio = time.time()

# Ordenar o array com bubble sort
bubble_sort(array)

# Marcar o tempo depois da ordenação
fim = time.time()

# Calcular e exibir o tempo gasto
tempo_gasto = fim - inicio
print(f"Tempo gasto para ordenar o array: {tempo_gasto:.6f} segundos")