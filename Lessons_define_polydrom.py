def polydrom_check(number):
    number = str(number)
    s_list = list(number)
    s_list.reverse()
    reverse_number = ''.join(s_list)
    return number == reverse_number

number_user = input("Please enter number: ")

if polydrom_check(number_user):
    print(f"Our {number_user} is polydrom")
else:
    print(f"Our {number_user} is not polydrome")

def reverse_string(text):
    list_text = list(text)
    list_text.reverse()
    reverse_text = ''.join(list_text)
    return reverse_text

enter_text = input("Please enter your message: ")
print(f"Reverse string {reverse_string(enter_text)}")

def count_strings(strings):
    count = 0
    for s in strings:
        if len(s) > 5:
            count += 1
    return count

strings = ["We all go to home", "my birhday", "our fucking life", "shit"]
print(f"{count_strings(strings)}")



