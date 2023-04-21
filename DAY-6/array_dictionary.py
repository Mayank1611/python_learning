my_dict = {
    "array1": [1, 2, 3, 4],
    "array2": ["a", "b", "c"],
    "array3": [1.1, 2.2, 3.3],
}

print(my_dict["array1"])
print(my_dict["array2"])
print(my_dict["array3"])

my_dict["array4"] = [True, False, True]

my_dict["array1"] = [5, 6, 7, 8]

del my_dict["array2"]

if "array3" in my_dict:
    print("array3 exists in the dictionary.")

print(my_dict)
