def pesquisa_binaria(item, lista):
    baixo = 0
    alto = len(lista) - 1
    while(baixo<=alto):
        meio = (baixo+alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [num for num in range(2,100,2)]
print(pesquisa_binaria(78, minha_lista))
print(pesquisa_binaria(13, minha_lista))
