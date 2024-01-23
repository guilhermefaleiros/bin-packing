import time
import random

# Define a função que verifica se é possível acomodar os itens em um número fixo de bins
def bin_packing(items, bin_capacity, bin_count):
    items.sort(reverse=True)  # Ordena os itens em ordem decrescente para otimizar a alocação
    
    # Inicializa a lista que armazena a capacidade restante para cada bin
    bin_rem = [bin_capacity] * bin_count

    # Itera por cada item na lista
    for item in items:
        # Encontra o primeiro bin que pode acomodar o item
        j = 0
        while(j < bin_count):
            if (bin_rem[j] >= item):  # Verifica se o bin atual tem capacidade para o item
                bin_rem[j] = bin_rem[j] - item  # Aloca o item no bin, atualizando a capacidade restante
                break
            j += 1

        # Se o item não coube em nenhum bin existente, a alocação é impossível
        if (j == bin_count):
            return False  # Retorna False, pois não foi possível acomodar o item

    # Se todos os itens foram acomodados, retorna True
    return True

times = []
max_time = 0

BINS = 6
INPUT_SIZE = 10
BIN_CAPACITY = 10

for _ in range(10):
    items = [random.randint(1, 10) for _ in range(INPUT_SIZE)]

    start_time = time.time()
    can_pack = bin_packing(items, BIN_CAPACITY, BINS)
    execution_time = (time.time() - start_time) * 1000

    if execution_time > max_time:
        max_time = execution_time
    
    times.append(execution_time)

    print(f"Pode alocar todos os itens em {BINS} compartimentos? {'Sim' if can_pack else 'Não'}")
    print(f"Tempo de execução: {execution_time:.3f}ms")

print(f"Tempo médio de execução: {sum(times) / len(times):.3f}ms")
print(f"Maior tempo de execução: {max_time:.3f}ms")