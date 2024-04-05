import random
import time

def quicksort_pivot_first():
    data_list = [8, 9, 10, 11, 12, 16, 17, 18, 13, 14, 15, 19, 20, 1, 2, 6, 7, 21, 22]
    if len(data_list) <= 1:
        return data_list
    pivot = data_list[0]
    left = []
    right = []
    for item in data_list[1:]:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)

    return quicksort_pivot_first(left) + [pivot] + quicksort_pivot_first(right)


def quicksort_pivot_middle():
    data_list = [8, 9, 10, 11, 12, 16, 17, 18, 13, 14, 15, 19, 20, 1, 2, 6, 7, 21, 22]
    if len(data_list) <= 1:
        return data_list
    pivot = data_list[len(data_list)//2]
    left = []
    right = []
    for item in data_list:
        if item <= pivot and not item is pivot:
            left.append(item)
        elif not item is pivot:
            right.append(item)

    return quicksort_pivot_middle(left) + [pivot] + quicksort_pivot_middle(right)



start_time1 = time.time()
result1 = quicksort_pivot_first()
print(time.time() - start_time1)

print("----------------------------------------------------------------")
start_time2 = time.time()
result2 = quicksort_pivot_middle()
print(time.time() - start_time2)

print(result1, result2)
