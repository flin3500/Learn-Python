students = [
    {"name": "lin",
     "age": 20,
     "gender": True,
     "height": 1.7,
     "weight": 75.0},
    {"name": "frank",
     "age": 19,
     "gender": False,
     "height": 1.6,
     "weight": 45.0},
]

find_name = "lin"

for stu_dict in students:

    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("found")
        break

else:
    print("not found")

print("end")