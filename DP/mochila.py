def knapsack_01(values, weights, capacity):
    n = len(values)
    
    # Criando a tabela para armazenar os resultados
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Preenchendo a tabela
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    # O valor máximo que pode ser carregado na mochila
    max_value = dp[n][capacity]
    
    # Encontrando os itens que foram incluídos na solução
    w = capacity
    items_selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items_selected.append(i-1)
            w -= weights[i-1]
    
    return max_value, items_selected

# Exemplo de uso
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, items_selected = knapsack_01(values, weights, capacity)
print(f"Valor máximo: {max_value}")
print(f"Itens selecionados: {items_selected}")