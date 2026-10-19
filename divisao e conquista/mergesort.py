def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontra o meio do array
        L = arr[:mid]        # Divide o array em duas metades
        R = arr[mid:]

        merge_sort(L)       # Ordena a primeira metade
        merge_sort(R)       # Ordena a segunda metade

        i = j = k = 0

        # Combina as duas metades de forma ordenada
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Verifica se ainda há elementos restantes em L ou R
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Exemplo de uso:
arr = [12, 11, 13, 5, 6, 7, 13]
print("Array original:", arr)
merge_sort(arr)
print("Array ordenado:", arr)