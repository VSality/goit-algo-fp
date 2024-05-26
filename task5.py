import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def bfs(tree_root):
    queue = deque([tree_root])
    visited = set()
    color = 0
    current_color = 1.0

    while queue:
        node = queue.popleft()
        if node.id not in visited:
            visited.add(node.id)
            
            color = plt.cm.Blues(current_color)  # Використання градієнта від темно-синього до світло-синього
            node.color = f'#{int(color[0] * 255):02x}{int(color[1] * 255):02x}{int(color[2] * 255):02x}'
            current_color -= 0.15
            
            print(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
                
def dfs(tree_root):
    stack = [tree_root]
    visited = set()
    color = 0
    current_color = 1.0

    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            
            color = plt.cm.Blues(current_color)  # Використання градієнта від темно-синього до світло-синього
            node.color = f'#{int(color[0] * 255):02x}{int(color[1] * 255):02x}{int(color[2] * 255):02x}'
            current_color -= 0.15

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

bfs(root)

# Відображення дерева після BFS
draw_tree(root)

dfs(root)

# Відображення дерева після DFS
draw_tree(root)