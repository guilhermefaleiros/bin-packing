import time
import random

# Recebe como parâmetro uma lista de itens e a capacidade de cada bin
def bin_packing(items, bin_capacity):
    # Ordena os itens em ordem decrescente
    sorted_items = sorted(items, reverse=True)

    bins = []

    # Passa por todos os items da lista e tenta acomodar ele em um bin 
    # já existente ou cria um novo bin caso seja possível
    for item in sorted_items:
        placed = False
        for bin in bins:
            if sum(bin) + item <= bin_capacity:
                bin.append(item)
                placed = True
                break

        if not placed:
            bins.append([item])

    # Retorna o número de bins necessários
    return len(bins)

times = []
max_time = 0

INPUT_SIZE = 10
BIN_CAPACITY = 10

for _ in range(10):
    items = [random.randint(1, 10) for _ in range(INPUT_SIZE)]
    bin_capacity = 10

    start_time = time.time()
    min_bins = bin_packing(items, BIN_CAPACITY)
    execution_time = (time.time() - start_time) * 1000

    if execution_time > max_time:
        max_time = execution_time
    
    times.append(execution_time)

    print(f"Número mínimo de compartimentos: {min_bins}")
    print(f"Tempo de execução: {execution_time:.3f} milissegundos")


print(f"Tempo médio de execução: {sum(times) / len(times):.3f} milissegundos")
print(f"Maior tempo de execução: {max_time:.3f} milissegundos")