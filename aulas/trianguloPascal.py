def TP(i,j):
    if j==0 or i==j:
        return 1
    return TP(i-1,j-1) + TP(i-1,j)
    
print(TP(6,3))
