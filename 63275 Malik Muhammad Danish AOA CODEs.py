
# ---------------------------------------------------------------
# 1. SELECTION SORT
# ---------------------------------------------------------------
import time

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return comparisons, swaps

def run_experiment(name, original_list):
    times = []
   
    for _ in range(3):
        test_copy = list(original_list)
        start_time = time.time()
        comps, swaps = selection_sort(test_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    
    avg_time = sum(times) / 3
    print(f"Results for {name}:")
    print(f"- Avg Time: {avg_time:.8f} seconds")
    print(f"- Comparisons: {comps}")
    print(f"- Swaps: {swaps}")
    print(f"- Auxiliary Space: O(1) (In-place)")
    print("-" * 30)

run_experiment("5 Elements Sorted", [1, 2, 3, 4, 5])

run_experiment("5 Elements Reverse", [5, 4, 3, 2, 1])

run_experiment("100 Elements Sorted", list(range(1, 101)))

run_experiment("100 Elements Reverse", list(range(100, 0, -1)))

# ---------------------------------------------------------------
# 2. BuBBLE SORT SORT
# ---------------------------------------------------------------

import time

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        
        already_sorted = True
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                already_sorted = False
        
        if already_sorted:
            break
            
    return comparisons, swaps

def run_experiment(name, original_list):
    times = []
    for _ in range(3):
        test_copy = list(original_list)
        start_time = time.time()
        comps, swaps = bubble_sort(test_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    
    avg_time = sum(times) / 3
    print(f"Results for {name}:")
    print(f"- Avg Time: {avg_time:.8f} seconds")
    print(f"- Comparisons: {comps}")
    print(f"- Swaps: {swaps}")
    print(f"- Auxiliary Space: O(1) (In-place)")
    print("-" * 30)

run_experiment("5 Elements Sorted", [1, 2, 3, 4, 5])

run_experiment("5 Elements Reverse", [5, 4, 3, 2, 1])

run_experiment("100 Elements Sorted", list(range(1, 101)))

run_experiment("100 Elements Reverse", list(range(100, 0, -1)))

# ---------------------------------------------------------------
# 3. QUICK SORT 
# ---------------------------------------------------------------

import time

def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
            
    return comparisons, swaps

def run_experiment(name, original_list):
    
    try:
        times = []
        for _ in range(3):
            test_copy = list(original_list)
            start_time = time.time()
            comps, swaps = insertion_sort(test_copy)
            end_time = time.time()
            times.append(end_time - start_time)
        avg_time = sum(times) / 3
    except:
        avg_time = 0.0
        comps, swaps = insertion_sort(list(original_list))

    print(f"Results for {name}:")
    print(f"- Avg Time: {avg_time:.8f} seconds")
    print(f"- Comparisons: {comps}")
    print(f"- Swaps (Shifts): {swaps}")
    print(f"- Auxiliary Space: O(1) (In-place)")
    print("-" * 30)

run_experiment("5 Elements Sorted", [1, 2, 3, 4, 5])
run_experiment("5 Elements Reverse", [5, 4, 3, 2, 1])

run_experiment("100 Elements Sorted", list(range(1, 101)))

run_experiment("100 Elements Reverse", list(range(100, 0, -1)))

 ---------------------------------------------------------------
# 4. MERGE SORT 
# ---------------------------------------------------------------

import time

def merge_sort_tracker(arr):
    stats = {"comps": 0, "swaps": 0}

    def merge_sort(data):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            # Recursive calls
            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0

            # Copy data to temp arrays and merge
            while i < len(left_half) and j < len(right_half):
                stats["comps"] += 1
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                stats["swaps"] += 1 # In Merge Sort, this is a 'write' operation
                k += 1

            # Checking if any element was left
            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1
                stats["swaps"] += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1
                stats["swaps"] += 1

    merge_sort(arr)
    return stats["comps"], stats["swaps"]

def run_experiment(name, original_list):
    times = []
    for _ in range(3):
        test_copy = list(original_list)
        start_time = time.time()
        comps, swaps = merge_sort_tracker(test_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    
    avg_time = sum(times) / 3
    print(f"Results for {name}:")
    print(f"- Avg Time: {avg_time:.8f} seconds")
    print(f"- Comparisons: {comps}")
    print(f"- Swaps (Writes): {swaps}")
    print(f"- Auxiliary Space: O(n)")
    print("-" * 30)

run_experiment("5 Elements Sorted", [1, 2, 3, 4, 5])

run_experiment("5 Elements Reverse", [5, 4, 3, 2, 1])

run_experiment("100 Elements Sorted", list(range(1, 101)))

run_experiment("100 Elements Reverse", list(range(100, 0, -1)))