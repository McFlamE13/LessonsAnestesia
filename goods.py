products = [
    {"id": 1, "price": 100, "category": "A"},
    {"id": 2, "price": 200, "category": "B"},
    {"id": 3, "price": 50, "category": "A"},
    {"id": 4, "price": 1000, "category": "C"},
    {"id": 5, "price": 250, "category": "A"},
    {"id": 6, "price": 500, "category": "B"},
    {"id": 7, "price": 200, "category": "C"},
    {"id": 8, "price": 4500, "category": "B"}
]
m_price = {}
for product in products:
    category = product["category"]
    if category not in m_price:
        m_price[category] = {"sum": 0, "count": 0}
    m_price[category]["sum"] += product["price"]
    m_price[category]["count"] += 1
for k, v in m_price.items():
    average = v["sum"] / v["count"]
    print(f"Average price for {k} - {average}")

max_price = {}
for product in products:
    category = product["category"]
    if category not in max_price or product["price"] > max_price[category]["price"]:
        max_price[category] = product
for k, v in max_price.items():
    print(f"{k} - id = {v['id']} price = {v['price']}")

price_together = 0 # переменная, куда будем складывать цену всех товаров
for product in products: # перебираем список товаров (словарей)
    price_together += product["price"] # складываем значения ключа "price" в переменной
print(f"Total amount of goods - {price_together}")




