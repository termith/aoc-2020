with open('input') as f:
    data = list(map(int, f.readlines()))
    data.sort()

current_adpt = 0
idx = 0
counter = [0, 0, 0]

while idx < len(data):
    cnt_idx = data[idx] - current_adpt
    counter[cnt_idx - 1] += 1
    current_adpt = data[idx]
    idx += 1

print(counter[0] * (counter[2] + 1))

data = [0] + data

# Количество путей в каждую вершину
paths = [1] + [0] * (len(data) - 1)
for i, adapter in enumerate(data):
    # Число путей в каждую вершину = сумме путей во все вершины, из которых можно в нее попасть
    # Так как попасть в каждую можно максимум из 3х предыдущих - мы проверяем только их
    # Проверяем 3 предыдущих вершины
    for j in range(i - 3, i):
        # если из предыдущей вершины можно попасть в текущую
        if (adapter - data[j]) <= 3:
            # Эта проверка "можно ли попасть из вершины data[j] в вершину adapter"
            # Случай первых вершин специально не обрабатываем
            paths[i] += paths[j]

print(paths[-1])
