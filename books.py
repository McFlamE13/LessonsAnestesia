books = {
    "1984": {"author": "George Orwell", "year": 1949},
    "Brave New World": {"author": "Aldous Huxley", "year": 1932}
}

books["Fahrenheit 451"] = {"author": "Ray Bradbury", "year": 1953}
books["1984"]["year"] = 1948

for title, info in books.items():
    print(f"{title} - {info['author']}, {info['year']}")