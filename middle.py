numbers = []
while True:
    num = input("Введитe какое-либо число или 'end': ")
    if num == "end":
        break
    if not num.isdigit():
        print("Введите число или 'end'")
    else:
        num = int(num)
        numbers.append(num)
average = sum(numbers) / len(numbers)
below = []
equal = []
above = []
for num in numbers:
    if num > average:
        below.append(num)
    elif num == average:
        equal.append(num)
    else:
        above.append(num)
print(f"Среднее значение = {average}")
print(f"Числа большe среднего: {below}")
print(f"Числа равные среднему: {equal}")
print(f"ЧИсла меньше среднего: {above}")
     