import turtle
import math

def draw_tree(branch_length, level, t):
    if level == 0:
        return
    
    # Малюємо основну гілку
    t.forward(branch_length)
    
    # Зберігаємо позицію та кут, щоб повернутися назад
    position = t.position()
    heading = t.heading()
    
    # Малюємо ліву гілку
    t.left(45)
    draw_tree(branch_length * math.cos(math.radians(45)), level - 1, t)
    
    # Повертаємося назад до основної гілки
    t.setposition(position)
    t.setheading(heading)
    
    # Малюємо праву гілку
    t.right(45)
    draw_tree(branch_length * math.cos(math.radians(45)), level - 1, t)
    
    # Повертаємося назад до основної гілки
    t.setposition(position)
    t.setheading(heading)

def main():
    # Налаштовуємо черепашку
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    
    level = 8
    branch_length = 100  # Довжина початкової гілки
    
    draw_tree(branch_length, level, t)
    turtle.done()

if __name__ == "__main__":
    main()
