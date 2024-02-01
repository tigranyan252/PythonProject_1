def find_oldest_parallel(arr):
    max_students = 0
    oldest_parallel = 0
    for i, students in enumerate(arr):
        if students > max_students:
            max_students = students
            oldest_parallel = i + 5
    return oldest_parallel

arr = [100, 80, 120, 150, 110, 90, 130]
oldest_parallel = find_oldest_parallel(arr)
print("Самая старшая параллель:", oldest_parallel)

import numpy as np

def insert_zero_columns(arr, k):
    new_arr = np.insert(arr, k, 0, axis=1)
    new_arr = np.insert(new_arr, k+2, 0, axis=1)
    return new_arr

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

new_arr = insert_zero_columns(arr, 1)
print(new_arr)

def swap_min_max(lst):
    min_val = min(lst)
    max_val = max(lst)
    min_idx = lst.index(min_val)
    max_idx = lst.index(max_val)
    lst[min_idx], lst[max_idx] = max_val, min_val
    return lst

lst = [1, 5, 3, 8, 2, 7]
new_lst = swap_min_max(lst)
print(new_lst)

def to_set(data):
    s = set(data)
    return s, len(s)


data = [1, 2, 2, 3, 4, 5, 5]
s, size = to_set(data)
print("Множество:", s)
print("Мощность множества:", size)

from collections import defaultdict


def count_sales(data):
    customers = defaultdict(lambda: defaultdict(int))
    for line in data:
        customer, product, quantity = line.split()
        customers[customer][product] += int(quantity)

    sorted_customers = sorted(customers.keys())
    for customer in sorted_customers:
        print("Покупатель:", customer)
        for product, quantity in sorted(customers[customer].items()):
            print("Товар:", product, "- Количество:", quantity)


data = ["Покупатель1 товар1 5",
        "Покупатель1 товар2 3",
        "Покупатель2 товар1 2",
        "Покупатель2 товар3 4",
        "Покупатель3 товар2 1"]

count_sales(data)