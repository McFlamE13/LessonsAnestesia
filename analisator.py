purchases = {}
while True:
    print("<<<Меню>>>")
    print("1. Добавить трату.")
    print("2. Общая сумма расходов.")
    print("3. Сумма максимальной покупки.")
    print("4. Средний расход по категориям.")
    print("5. Суммы трат по категориям.")
    print("6. Выход.")
    choice = int(input("Выберите пункт меню (1-6): "))
    if choice == 1:
        category = input("Введите категорию трат: ")
        amount = float(input("Сумма: "))
        if category not in purchases:
            purchases[category] = []
        purchases[category].append(amount)
        print(f"Добавлена категория {category} на сумму {amount}")
    elif choice == 2:
        total = 0
        for amounts in purchases.values():
            total += sum(amounts)
        print(f"Общая сумма расходов = {total}")
    elif choice == 3:
        max_amount = 0
        max_category = ""
        for category, amounts in purchases.items():
            tmp_max = max(amounts)
            if tmp_max > max_amount:
                max_amount = tmp_max
                max_category = category
        print(f"Максимальная трата {max_amount} в категории {max_category}")
    elif choice == 4:
        averages = {}
        for category, amounts in purchases.items():
            averages[category] = sum(amounts) / len(amounts)
        for k, v in averages.items():
            print(f"Для категории {k} средний расход - {v}")
    elif choice == 5:
        averages = {}
        for category, amounts in purchases.items():
            averages[category] = sum(amounts)
        for k, v in averages.items():
            print(f"Всего потрачено в категории {k} - {v}")
    elif choice == 6:
        print("Работа завершена")
        break
    else:
        print("Некорректный ввод!")

  