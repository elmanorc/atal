def f(x):
    if x<=1:
        return 1
    elif x%3==0:
        return x * (f(x-1))
    elif x%3==1:
        return x * (f(x-1)+1)
    else:
        return x * (f(x-1)+2)
print(f(5))
