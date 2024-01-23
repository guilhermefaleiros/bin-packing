import time
import random

def bin_packing(items, bin_capacity):
    # Função de backtracking para encontrar o número mínimo de compartimentos
    def backtrack(index, bins):
        # Se todos os itens foram alocados, retorna o número atual de compartimentos
        if index == len(items):
            return len(bins)

        # Item atual a ser alocado
        item = items[index]
        # Inicializa o número mínimo de compartimentos como infinito
        min_bins = float('inf')

        # Tenta colocar o item em cada um dos compartimentos existentes
        for i in range(len(bins)):
            if bins[i] + item <= bin_capacity:
                # Se o item couber, adiciona ao compartimento
                bins[i] += item
                # Recursivamente tenta alocar os próximos itens e atualiza o mínimo de compartimentos necessário
                min_bins = min(min_bins, backtrack(index + 1, bins))
                # Desfaz a adição do item ao compartimento (backtracking)
                bins[i] -= item

        # Tenta criar um novo compartimento para o item
        bins.append(item)
        # Recursivamente tenta alocar os próximos itens com o novo compartimento
        min_bins = min(min_bins, backtrack(index + 1, bins))
        # Remove o compartimento criado (backtracking)
        bins.pop()

        return min_bins
    
    # Ordena os itens em ordem decrescente para otimização
    items.sort(reverse=True)
    # Inicia o backtracking com o primeiro item e sem compartimentos
    return backtrack(0, [])


times = []
max_time = 0

INPUT_SIZE = 10
BIN_CAPACITY = 10

for _ in range(10):
    items = [random.randint(1, 10) for _ in range(INPUT_SIZE)]

    start_time = time.time()
    min_bins = bin_packing(items, BIN_CAPACITY)
    execution_time = (time.time() - start_time) * 1000

    if execution_time > max_time:
        max_time = execution_time
    
    times.append(execution_time)

    print(f"Número mínimo de compartimentos: {min_bins}")
    print(f"Tempo de execução: {execution_time:.3f} milissegundos")


print(f"Tempo médio de execução: {sum(times) / len(times):.3f}ms")
print(f"Maior tempo de execução: {max_time:.3f}ms")