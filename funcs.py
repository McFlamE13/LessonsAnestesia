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

user_commands = [
    ("right", 5),
    ("forward", 3),
    ("left", 2),
    ("backward", 6)
]
print(robot(user_commands))
