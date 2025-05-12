import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def find_connected_components(adjacency_matrix):
    n = len(adjacency_matrix)
    visited = [False] * n
    components = []
    
    for vertex in range(n):
        if not visited[vertex]:
            # Новая компонента связности
            component = []
            queue = deque([vertex])
            visited[vertex] = True
            component.append(vertex)
            
            # BFS для обхода всей компоненты
            while queue:
                current = queue.popleft()
                for neighbor in range(n):
                    if adjacency_matrix[current][neighbor] == 1 and not visited[neighbor]:
                        visited[neighbor] = True
                        component.append(neighbor)
                        queue.append(neighbor)
            
            components.append(component)
    
    return components

# Пример матрицы смежности для графа на изображении
# Индексы с 0, поэтому вершины 1-6 на изображении соответствуют 0-5 в коде
adjacency_matrix = [
    [0, 1, 1, 0, 0, 0],  # Вершина 1 (индекс 0)
    [1, 0, 0, 1, 0, 0],  # Вершина 2 (индекс 1)
    [1, 0, 0, 0, 1, 0],  # Вершина 3 (индекс 2)
    [0, 1, 0, 0, 1, 0],  # Вершина 4 (индекс 3)
    [0, 0, 1, 1, 0, 1],  # Вершина 5 (индекс 4)
    [0, 0, 0, 0, 1, 0]   # Вершина 6 (индекс 5)
]

# Находим связные компоненты
components = find_connected_components(adjacency_matrix)

# Выводим результат
print("Найдено связных компонент:", len(components))
for i, component in enumerate(components):
    # Увеличиваем индексы на 1 для соответствия нумерации на изображении
    print(f"Компонента {i+1}:", [vertex+1 for vertex in component])

# Визуализируем граф с выделением компонент разными цветами
G = nx.Graph()
for i in range(len(adjacency_matrix)):
    G.add_node(i+1)  # Добавляем вершины с нумерацией с 1

for i in range(len(adjacency_matrix)):
    for j in range(i+1, len(adjacency_matrix)):
        if adjacency_matrix[i][j] == 1:
            G.add_edge(i+1, j+1)  # Добавляем рёбра с учётом нумерации с 1

# Визуализация
pos = nx.spring_layout(G, seed=42)
colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightpink']

node_colors = []
for node in G.nodes():
    # Находим компоненту, к которой принадлежит вершина
    for i, component in enumerate(components):
        if node-1 in component:
            node_colors.append(colors[i % len(colors)])
            break

nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=800, font_size=16)
plt.show()
