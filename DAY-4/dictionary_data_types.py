my_dict = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science", "History"],
    "scores": {"Math": 90, "Science": 85, "History": 92},
    1: "One",
    2.5: "Two point Five"
}

print(my_dict["name"])
print(my_dict["age"])
print(my_dict["is_student"])
print(my_dict["courses"])
print(my_dict["courses"][0])
print(my_dict["scores"]["Math"])
print(my_dict[1])
print(my_dict[2.5])
