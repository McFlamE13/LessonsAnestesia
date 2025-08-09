# функция для проверки простого числа
def number(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def robot(commands):
    x, y = 0, 0
    for direction, steps in commands:
        if direction == "left":
            x -= steps
        elif direction == "right":
            x += steps
        elif direction == "forward":
            y += steps
        elif direction == "backward":
            y -= steps
    return (x, y)

user_commands = []

steps = input("Сколько команд нужно выполнить? ")
if not steps.isdigit():
    print("Неверное значение")
else:
    steps = int(steps)
    for i in range(1, steps + 1):   
        action = input(f"Введите команду {i} (forward, backward, left, right): ")
        count = int(input("Введите количество шагов: "))
        user_commands.append((action, count))
print(robot(user_commands))

