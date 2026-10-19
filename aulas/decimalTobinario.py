def binario(decimal):
    if decimal==0 or decimal==1:
        return f'{decimal}'
    return binario(decimal//2) + str(decimal%2)
 
print(binario(19))
