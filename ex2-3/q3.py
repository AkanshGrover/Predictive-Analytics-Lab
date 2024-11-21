my_list = [1, 2, 3, 4]
print("Original list:", my_list)
my_list[2] = 99
print("Modified list:", my_list)
my_tuple = (1, 2, 3, 4)
print("Original tuple:", my_tuple)
try:
    my_tuple[2] = 99
except TypeError as e:
    print("Error:", e)
