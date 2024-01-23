from itertools import permutations
import random
import time

# Define a função que verifica se é possível acomodar os itens em um número fixo de bins
def bin_packing(items, bin_capacity, k):
    # Calcula o número total de itens
    n = len(items)
    # Ordena os itens em ordem decrescente
    items = sorted(items, reverse=True)
    
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
                # Se o número de contêineres exceder k, a resposta é não
                if bin_count > k:
                    break
        
        # Se a permutação atual usar k contêineres ou menos, a resposta é sim
        if bin_count <= k:
            return True
    
    # Se todas as permutações foram testadas e nenhuma coube em k contêineres ou menos, a resposta é não
    return False


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