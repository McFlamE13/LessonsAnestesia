def fac(n):
    if n < 0:
        print("Неверное число")
    if n == 1 or n == 0:
        return 1
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

user_fac = input("Введите число: ")
if not user_fac.isdigit():
    print("Неверное число")
else:
    user_fac = int(user_fac)
    print(f"Факториал {user_fac} = {fac(user_fac)}") 