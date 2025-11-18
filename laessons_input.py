def count_positive(numbers):
    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count

numbers = [3, -23, 10, 0, -234, 87, 99, -13]
print(f"{count_positive(numbers)}")

def count_values_above_threshold(data, threshold):
    count = 0
    for _, value in data.items():
        if value > threshold:
            count += 1
    return count

limit = 13
keys_numbers = {
"num_1": 3,
"num_2": 15,
"num_3": 67,
"num_4": 9,
"num_5": 124 
}

print(f"{count_values_above_threshold(keys_numbers, limit)}")

students =[{
    "name": "Sasha",
    "score": 6
}, 
{
    "name": "Alina",
    "score": 10
},
{
    "name": "Arslan",
    "score": 99
}]
min_score = 8
def filter_students(students, min_score):
    good_students = []
    for k in students:
        if k["score"] >= min_score:
            good_students.append(k["name"])
    return good_students
result = filter_students(students, min_score)
for names in result:
    print(names, end = ",")

#print(f"{filter_students(students, min_score)}")

