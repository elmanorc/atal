def recursive_fatorial(n):
    if n == 0:
        return 1
    else:
        print(f"Calculating {n}!")
        return n * recursive_fatorial(n - 1)

print(recursive_fatorial(5))