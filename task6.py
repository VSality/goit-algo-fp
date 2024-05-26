
class Item:
    def __init__(self, cost, calories, name):
        self.name = name
        self.cost = cost
        self.calories = calories
        self.ratio = calories / cost
        
K = None
def dynamic_programming(W, items: list[Item]):
    # створюємо таблицю K для зберігання оптимальних значень підзадач
    global K
    K = [[0 for w in range(W + 1)] for item in items]

    # будуємо таблицю K знизу вгору
    iter = 0
    for item in items:
        for w in range(W + 1):
            if iter == 0 or w == 0:
                K[iter][w] = 0
            elif items[iter - 1].cost <= w:
                add_value = items[iter - 1].calories
                add_name = items[iter - 1].name
                the_rest = K[iter - 1][w - items[iter - 1].cost]
                without = K[iter - 1][w]
                #print(item.name, w, ":", add_value, the_rest, without)
                K[iter][w] = max(add_value+the_rest, without)
            else:
                K[iter][w] = K[iter - 1][w]
        iter += 1

    return K[len(items) - 1][W]

def greedy_algorithm(items: list[Item], capacity: int) -> int:
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0
    for item in items:
        if capacity >= item.cost:
            capacity -= item.cost
            total_value += item.calories
            #print(capacity, total_value, item.name)
           
    return total_value

# Дані предметів
items = [Item(50, 300, "pizza"), Item(40, 250, "hamburger"), Item(30, 200, "hot-dog"), Item(10, 100, "pepsi"),
         Item(15, 220, "cola"), Item(25, 350, "potato")]
# Місткість рюкзака
capacity = 90

print("greedy eat calc", greedy_algorithm(items, capacity) , "calories")
print("dynamyc eat calc", dynamic_programming(capacity, items), "calories") 