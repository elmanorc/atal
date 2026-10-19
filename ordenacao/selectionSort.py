def ordena(L):
    m = len(L)
    for i in range(0,m-1):
        min = i
        for j in range(i+1, m):
            if L[j] < L[i]:
                min = j
        aux = L[min]
        L[min] = L[i]
        L[i] = aux
    return L
 
print(ordena([12, 11, 13, 5, 6, 7, 13]))