import time
import random

# Recebe como parâmetro uma lista de itens, a capacidade de cada bin e o número de bins
def bin_packing(items, bin_capacity, number_of_bins):

    # Preenche todos os bins existes peso 0
    bins = [0] * number_of_bins

    # Ordena os itens em ordem decrescente
    sorted_items = sorted(items, reverse=True)


    for item in sorted_items:
        placed = False
        for i in range(number_of_bins):
            if bins[i] + item <= bin_capacity:
                bins[i] += item
                placed = True
                break
        if not placed:
            return False
    
    # Retorna verdadeiro caso todos os itens tenham sido acomodados
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