import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]

def measure_time_sorting(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Тестирование сортировки пузырьком
arr_sizes = [1000, 5000, 10000]
for size in arr_sizes:
    arr = generate_random_array(size)
    time_taken = measure_time_sorting(bubble_sort, arr)
    print(f"Bubble Sort: Array size {size}, Time taken: {time_taken:.6f} seconds")

# Тестирование сортировки слиянием
for size in arr_sizes:
    arr = generate_random_array(size)
    time_taken = measure_time_sorting(merge_sort, arr)
    print(f"Merge Sort: Array size {size}, Time taken: {time_taken:.6f} seconds")
