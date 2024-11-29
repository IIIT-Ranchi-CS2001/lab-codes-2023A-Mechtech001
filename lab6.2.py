
def my_sort(data, key=0):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def my_zip(customer_names, customer_ids, shopping_points, strct=True):
    if strct:
        if len(customer_names) == len(customer_ids) == len(shopping_points):
            return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(len(customer_names))]
        else:
            raise ValueError("Lists are of unequal length. Zipping cannot proceed when strct=True.")
    else:
        min_length = min(len(customer_names), len(customer_ids), len(shopping_points))
        return [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(min_length)]
    
    
customer_names = ['Alice', 'Bob', 'Charlie']
customer_ids = [101, 103, 102]
shopping_points = [50, 70, 30]

data = my_zip(customer_names, customer_ids, shopping_points, strct=False)

sorted_by_name = my_sort(data, key=0)
print("Sorted by customer name:", sorted_by_name)

sorted_by_id = my_sort(data, key=1)
print("Sorted by customer ID:", sorted_by_id)

sorted_by_points = my_sort(data, key=2)
print("Sorted by shopping points:", sorted_by_points)
