def is_perfect_number(n):
    if n <= 0:
        return False
    
    sum = 0
    end = int(n ** 0.5)
    for i in range(2, end+1):
        if n % i == 0:
            sum += i
            if n // i != i:
                sum += n // i
    
    return sum == n

num = int(input("Numero:"))
print(is_perfect_number(num))