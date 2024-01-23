import time
import random

def bin_packing(items, bin_capacity):

    # Caso base: se há apenas um item ou nenhum, retorna esse número
    if len(items) <= 1:
        return len(items)

    # Ordena os itens em ordem decrescente
    items.sort(reverse=True)

    # Define os limites para classificar os itens como grandes, médios ou pequenos
    large_threshold = bin_capacity * 0.7
    medium_threshold = bin_capacity * 0.4

    # Divide os itens em três subconjuntos baseados nos limites definidos
    large_items = [item for item in items if item > large_threshold]
    medium_items = [item for item in items if medium_threshold < item <= large_threshold]
    small_items = [item for item in items if item <= medium_threshold]

    # Executa o algoritmo de first fit decreasing para cada subconjunto
    small_items_bins = first_fit_decreasing(small_items, bin_capacity)
    medium_items_bins = first_fit_decreasing(medium_items, bin_capacity)
    large_items_bins = first_fit_decreasing(large_items, bin_capacity)

    # Combina os compartimentos dos três subconjuntos
    combined_bins = combine_bins_variable(small_items_bins, medium_items_bins, large_items_bins, bin_capacity)

    # Retorna o número total de compartimentos necessários
    return len(combined_bins)

# Define a função que implementa o algoritmo First Fit Decreasing
def first_fit_decreasing(items, bin_capacity):
    # Ordena os itens em ordem decrescente
    items.sort(reverse=True)
    bins = []
    # Aloca os itens nos compartimentos
    for item in items:
        allocated = False
        for bin in bins:
            # Verifica se o item cabe no compartimento
            if sum(bin) + item <= bin_capacity:
                bin.append(item)
                allocated = True
                break
        # Se o item não couber em nenhum compartimento existente, cria um novo
        if not allocated:
            bins.append([item])
    # Retorna os compartimentos com os itens alocados
    return bins

# Define a função para combinar os compartimentos dos três subconjuntos
def combine_bins_variable(bins1, bins2, bins3, bin_capacity):
    combined_bins = bins1[:]
    # Combina os compartimentos dos subconjuntos
    for bin in bins2 + bins3:
        allocated = False
        for combined_bin in combined_bins:
            # Tenta adicionar os itens do compartimento atual em um compartimento combinado
            if sum(combined_bin) + sum(bin) <= bin_capacity:
                combined_bin.extend(bin)
                allocated = True
                break
        # Se os itens não couberem em nenhum compartimento combinado, cria um novo
        if not allocated:
            combined_bins.append(bin)
    # Retorna os compartimentos combinados
    return combined_bins


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