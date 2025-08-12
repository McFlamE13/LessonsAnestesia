num = int(input("Введите число: "))
sys = int(input("Введите основание системы счисления: "))
digits = "0123456789ABCDEF"
result = ""
if num == 0:
    result == 0
else:
    while num > 0:
        tmp = num % sys
        result = digits[tmp] + result
        num = num // sys
print(result)

