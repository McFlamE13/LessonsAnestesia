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
    choice = input("Выберите пункт меню (1 - 6): ")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            description = input("Ваша задача: ")
            tasks[id] = {"description": description, "status": "none"}
            operations.append(f"Добавлена задача - {description}")
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
        elif choice == 4:
            if not tasks:
                print("Задачи отсуствуют")
            else:
                print("Список задач:")
                for k, v in tasks.items():
                    print(f"[{k}] {v['description']} - {v['status']}")
                status_task_id = int(input("Введите номер задачи из списка выше, которую хотите завершить: "))
                if status_task_id in tasks:
                    tasks[status_task_id]["status"] = "done"
                    operations.append(f"Задача [{status_task_id}] отмеченна как выполненная")
                    print(f"Задача [{status_task_id}] отмеченна как выполненная")
                else:
                    print("Задача отсутсвует или вы ввели неверный номер задачи.")
        elif choice == 5:
            if not operations:
                print("Список операций пуст")
            else:
                for op in operations:
                    print(f"{op}")
        else:
            print("Ошибка: Введите число от 1 до 6.")
    else:
        print("Некорректно введен номер пункта меню")



    
    




        


        




