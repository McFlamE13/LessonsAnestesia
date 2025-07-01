tasks = {} # словарь для хранения задач
id = 1
operations = [] # список истории произведенных операций
while True:
    print("<<<Меню>>>")
    print("1. Добавить задачу.")
    print("2. Удалить задачу.")
    print("3. Просмотреть задачи.")
    print("4. Отметить как выполненную.")
    print("5 История действий.")
    print("6. Выход")
    choice = int(input("Выберите пункт меню (1 - 6): "))
    if choice == 1:
        description = input("Ваша задача: ")
        tasks[id] = {"description": description, "status": "none"}
        operations.append(f"Добавлена задача {description}")
        print(f"Задача {id} добавлена.")
        id += 1
    elif choice == 2:
        delete_id = int(input("Введите id задачи, которую хотите удалить: "))
        if delete_id in tasks:
            delete_task = tasks.pop(delete_id)
            print(f"Вы удалили задачу номер {delete_id}")
            operations.append(f"Удаление задачи номер {delete_id}")
        else:
            print("Номер такой задачи отсутсвует")
    elif choice == 3:
        if not tasks:
            print("Задачи отсуствуют")
        else:
            print("Список задач:")
            for k, v in tasks.items():
                print(f"[{k}] {v['description']} - {v['status']}")
    elif choice == 6:
        print("Работа завершена")
        break
        




