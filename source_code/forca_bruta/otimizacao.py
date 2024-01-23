from itertools import permutations
import time
import random

# Define a função bin_packing, que recebe uma lista de itens e a capacidade dos contêineres
def bin_packing(items, bin_capacity):
    # Calcula o número total de itens
    n = len(items)
    # Ordena os itens em ordem decrescente
    items = sorted(items, reverse=True)
    
    # Inicialmente, assume-se que cada item vai para um contêiner diferente
    best_bin_count = n
    
    # Gera todas as permutações possíveis para organizar os itens
    for bins in permutations(range(n)):
        # Inicializa a capacidade de cada contêiner com a capacidade máxima
        bin_capacities = [bin_capacity] * n
        # Inicializa o contador de contêineres usados
        bin_count = 0
        
        # Itera sobre cada índice de item na permutação atual
        for item_index in bins:
            # Obtém o item correspondente ao índice
            item = items[item_index]
            # Verifica se o item cabe em algum dos contêineres já abertos
            for i in range(bin_count):
                # Se o item couber no contêiner, subtrai a capacidade do contêiner
                if bin_capacities[i] >= item:
                    bin_capacities[i] -= item
                    break
            else:
                # Se o item não couber em nenhum contêiner, abre um novo contêiner
                bin_count += 1
                bin_capacities[bin_count - 1] -= item
        
        # Atualiza o melhor número de contêineres, se a permutação atual usar menos contêineres
        best_bin_count = min(best_bin_count, bin_count)
    
    # Retorna o menor número de contêineres necessário para acomodar todos os itens
    return best_bin_count

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