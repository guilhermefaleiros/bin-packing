import time
import random

# Define a função que implementa o algoritmo de bin packing
def bin_packing(items, bin_capacity):
    n = len(items)  # Calcula o número total de itens
    items.sort(reverse=True)  # Ordena os itens em ordem decrescente para otimizar a alocação
    
    # Inicializa o número de bins necessários
    bin_count = 0
    
    # Inicializa a lista que armazena a capacidade restante para cada bin
    bin_rem = [0] * n

    # Itera por cada item na lista
    for item in items:
        # Encontra o primeiro bin que pode acomodar o item
        j = 0
        while(j < bin_count):
            if (bin_rem[j] >= item):  # Verifica se o bin atual tem capacidade para o item
                bin_rem[j] = bin_rem[j] - item  # Aloca o item no bin, atualizando a capacidade restante
                break
            j += 1

        # Se nenhum bin existente puder acomodar o item, cria um novo bin
        if (j == bin_count):
            bin_rem[j] = bin_capacity - item  # Aloca o item no novo bin, inicializando a capacidade restante
            bin_count += 1  # Incrementa o contador de bins

    # Retorna o número total de bins necessários para acomodar todos os itens
    return bin_count


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
