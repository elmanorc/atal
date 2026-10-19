def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    # Comparar elementos e juntar em ordem
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # Adicionar elementos restantes
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

# Exemplo de uso:
if __name__ == "__main__":
    lista = [3, 5, 6, 1, 8, 7, 2, 4]
    print("Lista original:", lista)
    lista_ordenada = merge_sort(lista)
    print("Lista ordenada:", lista_ordenada)
