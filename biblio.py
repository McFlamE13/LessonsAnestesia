counter = 2
def generate_id():
  global counter
  counter += 1
  return f"B-{counter:03d}"

user_counter = 101
def generate_uid():
    global user_counter
    user_counter += 1
    return f"U-{user_counter}"

def add_user():
   user_name = input("Введите имя пользователя")
   user_id = generate_uid()
   users[user_id] = {"name": user_name, "borrowed": []}
   print(f"Пользователь с id {user_id} добавлен")

def borrow_book():
   user_id = input("Введите id пользователя: ")
   book_id = input("Введите id книги: ")
   if user_id not in users:
      print("Пользователь не найден")
      return
   if book_id not in books:
      print("Книга не найдена")
      return
   if not books[book_id]["available"]:
      print("Книга уже выдана")
      return
   books[book_id]["available"] = False
   users[user_id]["borrowed"].append(book_id)

def return_book():
   book_id = input("Введите id книги: ")
   if book_id not in books:
      print("Книга не найдена")
      return
   if books[book_id]["available"]:
      print("Книга в библиотеке")
      return
   books[book_id]["available"] = True
   for user_id, user_data in users.items():
      if book_id in user_data["borrowed"]:
         user_data["borrowed"].remove(book_id)
         print(f"Книга с id {book_id} возвращена пользователем {user_data['name']}")
         return
   print("Книга не найдена")
  
def delete_user():
   user_id = input("Введите id пользователя для удаления: ")
   if user_id not in users:
      print("Пользователь не найден")
      return
   if users[user_id]["borrowed"]:
      print("Нельзя удалить пользователя, у которого есть не возвращенные книги")
      return
   del users[user_id]
   print(f"Пользователь с id {user_id} удален")

def all_books():
   for k, v in books.items():
    if v["available"]:
       print(f"ID: {k}, Название: {v['title']}, Автор книги: {v['author']},  Наличие: 'Есть'")
    else:
     print(f"ID: {k},  Название: {v['title']},  Автор книги: {v['author']},  Наличие: 'Нет'")

def available_books():
   print("Доступные книги:")
   for k, v in books.items():
      if v["available"]:
         print(f"Название: {v['title']}, Автор книги: {v['author']}")

def user_books():
    print("Книги у пользователей:")
    for k, v in users.items:
       if not v["borrowed"]:
          print(f"Пользователь с ID {k} под именем {v['name']} взял книгу/книги - {v['borrowed']}")
           
def add_book():
  title = input("Введите название книги: ")
  author = input("Введите фамилию автора книги: ")
  id = generate_id()
  books[id] = {"title": title, "author": author, "available": True}
  print(f"Книга c id {id} добавлена")

books = {
  "B-001": {"title": "Python Basics", "author": "A. Smith", "available": True},
  "B-002": {"title": "Data Science", "author": "B. Johnson", "available": False}
}

users = {
  "U-100": {"name": "Alice", "borrowed": ["B-002"]},
  "U-101": {"name": "Bob", "borrowed": []}
}

while True:
    print("\nГлавное меню:")
    print("1. Добавить книгу")
    print("2. Добавить пользователя")
    print("3. Удалить пользователя")
    print("4. Выдать книгу")
    print("5. Вернуть книгу")
    print("6. Показать вообще все списки в библиотеке")
    print("7. Показать книги в наличиии")
    print("8. Какой пользователь какие книги взял")
    print("0. Выход")
    choice = input("Выберите действие: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        add_user()
    elif choice == "3":
        delete_user()
    elif choice == "4":
        borrow_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        all_books()
    elif choice == "7":
        available_books()
    elif choice == "8":
        user_books()
    elif choice == "0":
        print("Выход из программы")
        break
    else:
        print("Неверный ввод, попробуйте снова")
