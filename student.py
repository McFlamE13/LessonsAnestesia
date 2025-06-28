student = {
    "name": "FlamE",
    "age": 38,
    "subjects": ["math", "history", "biology"]
}
print(f"{student['subjects'][0]}")
student["grade"] = "A"
del student["age"]
for k, v in student.items():
    if k != "subjects":
        print(f"{k}: {v}")
    else:
        print("subjects: ")
        for s in v:
            print(f"\t- {s}")

      