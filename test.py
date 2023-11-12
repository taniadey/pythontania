my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
replacement_values = [10, 20, 30]

keys_to_replace = ["b", "d"]

for key in keys_to_replace:
    if key in my_dict:
        my_dict[key] = replacement_values.pop(0)

print(my_dict)
