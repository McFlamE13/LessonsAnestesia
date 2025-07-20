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

borrow_book()