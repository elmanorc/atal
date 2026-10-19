import random

# Lista de números gerados pelo PRNG
numbers = [2991312382, 3062119789, 1228959102, 1840268610, 974319580]

# Tentar descobrir a semente testando várias até que corresponda
for seed in range(2**32):
    random.seed(seed)
    
    # Gerar a mesma quantidade de números e comparar
    generated = [random.getrandbits(32) for _ in range(len(numbers))]
    
    if generated == numbers:
        print(f"A semente é: {seed}")
        break