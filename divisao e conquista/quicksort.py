def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

def funcao(x):

    if x<=1:
        return 1
    else:
        return x * (funcao(x-1) + funcao(x-2))
print(funcao(5))

#print(quicksort([10, 5, 2, 3]))