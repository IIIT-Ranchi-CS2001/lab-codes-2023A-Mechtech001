
def my_max(*args):
    if len(args) == 0:
        raise ValueError("Empty container passed.")
    max_value = args[0]
    for num in args[1:]:
        if num > max_value:
            max_value = num
    return max_value

my_list = [3, 5, 7, 2, 8]
print("Maximum in list:", my_max(*my_list))

my_set = {4, 9, 1, 6}
print("Maximum in set:", my_max(*my_set))

my_tuple = (10, 15, 8, 20, 13)
print("Maximum in tuple:", my_max(*my_tuple))
