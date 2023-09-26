random_list = [105, 3.1, "Hello", 737, "Python", "World", 412, 5.5, "AI"]

int_dictionary = {"satuan": [], "puluhan": [], "ratusan": []}
float_tuple = ()
string_list = []

for item in random_list:
    if isinstance(item, int):
        if item < 10:
            int_dictionary["satuan"].append(item)
        elif item < 100:
            int_dictionary["puluhan"].append(item)
        else:
            int_dictionary["ratusan"].append(item)
    elif isinstance(item, float):
        float_tuple += (item,)
    elif isinstance(item, str):
        string_list.append(item)

print("Integer (Satuan):", int_dictionary["satuan"])
print("Integer (Puluhan):", int_dictionary["puluhan"])
print("Integer (Ratusan):", int_dictionary["ratusan"])
print("Float Tuple:", float_tuple)
print("String List:", string_list)
