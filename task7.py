import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}  # словник для підрахунку кількості випадінь кожної суми
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)  # кидаємо перший кубик
        dice2 = random.randint(1, 6)  # кидаємо другий кубик
        total = dice1 + dice2  # обчислюємо суму чисел на кубиках
        sums_count[total] += 1  # збільшуємо лічильник для цієї суми
    return sums_count

def calculate_probability_monte_carlo(sums_count, num_rolls):
    probabilities = {}
    for total, count in sums_count.items():
        probability = count / num_rolls
        probabilities[total] = probability*100
    return probabilities

def plot_probabilities(probabilities):
    plt.bar(probabilities.keys(), probabilities.values(), color='skyblue')
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність %')
    plt.title('Ймовірності сум чисел при киданні двох кубиків')
    plt.xticks(range(2, 13))
    plt.show()


def main(num_rolls):
    sums_count = simulate_dice_rolls(num_rolls)
    probabilities = calculate_probability_monte_carlo(sums_count, num_rolls)
    plot_probabilities(probabilities)
    print(probabilities)
 

if __name__ == "__main__":
    num_rolls = 1000  # кількість кидків кубиків для симуляції
    main(num_rolls)
