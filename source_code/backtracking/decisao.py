import time
import random

def bin_packing(items, bin_capacity, k):
    # Função de backtracking para verificar se é possível alocar todos os itens em k compartimentos
    def backtrack(index, bins, k):
        # Se todos os itens foram alocados, retorna True
        if index == len(items):
            return True

        # Item atual a ser alocado
        item = items[index]

        # Tenta colocar o item em cada um dos compartimentos existentes
        for i in range(len(bins)):
            if bins[i] + item <= bin_capacity:
                # Se o item couber, adiciona ao compartimento
                bins[i] += item
                # Recursivamente tenta alocar os próximos itens
                if backtrack(index + 1, bins, k):
                    return True
                # Desfaz a adição do item ao compartimento (backtracking)
                bins[i] -= item

        # Se ainda houver espaço para criar um novo compartimento
        if len(bins) < k:
            # Tenta criar um novo compartimento para o item
            bins.append(item)
            # Recursivamente tenta alocar os próximos itens com o novo compartimento
            if backtrack(index + 1, bins, k):
                return True
            # Remove o compartimento criado (backtracking)
            bins.pop()

        # Se não foi possível alocar o item em nenhum compartimento, retorna False
        return False
    
    # Ordena os itens em ordem decrescente para otimização
    items.sort(reverse=True)
    # Inicia o backtracking com o primeiro item e sem compartimentos
    return backtrack(0, [], k)


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