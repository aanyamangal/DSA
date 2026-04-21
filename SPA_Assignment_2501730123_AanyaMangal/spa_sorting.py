import random
import time


# 1. Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr



# 2. Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# 3. Quick Sort 

def quick_sort(arr, low, high):
    while low < high:
        pi = partition(arr, low, high)

        # Recurse on smaller part first (prevents deep recursion)
        if pi - low < high - pi:
            quick_sort(arr, low, pi - 1)
            low = pi + 1
        else:
            quick_sort(arr, pi + 1, high)
            high = pi - 1


def partition(arr, low, high):
    # Random pivot (prevents worst case)
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Timing Function

def measure_time(sort_func, arr, is_quick=False):
    arr_copy = arr.copy()

    start = time.time()

    if is_quick:
        sort_func(arr_copy, 0, len(arr_copy) - 1)
    else:
        sort_func(arr_copy)

    end = time.time()

    return (end - start) * 1000  # milliseconds



# Dataset Generator

def generate_datasets():
    sizes = [1000, 5000, 10000]
    datasets = {}

    random.seed(42)

    for size in sizes:
        datasets[(size, "random")] = [random.randint(1, 100000) for _ in range(size)]
        datasets[(size, "sorted")] = list(range(size))
        datasets[(size, "reverse")] = list(range(size, 0, -1))

    return datasets

# Correctness Check

def check_correctness():
    test = [5, 2, 9, 1, 5, 6]

    print("Correctness Check:")
    print("Original:", test)

    print("Insertion:", insertion_sort(test.copy()))
    print("Merge:", merge_sort(test.copy()))

    q = test.copy()
    quick_sort(q, 0, len(q) - 1)
    print("Quick:", q)

    print("-" * 50)



# Main Function

def main():
    check_correctness()

    datasets = generate_datasets()

    results = []

    print("Sorting Performance Results (in ms)")
    print("=" * 60)

    for (size, dtype), data in datasets.items():
        print(f"\nDataset: {dtype.upper()}, Size: {size}")

        t1 = measure_time(insertion_sort, data)
        print(f"Insertion Sort: {t1:.2f} ms")

        t2 = measure_time(merge_sort, data)
        print(f"Merge Sort: {t2:.2f} ms")

        t3 = measure_time(quick_sort, data, is_quick=True)
        print(f"Quick Sort: {t3:.2f} ms")

        results.append((size, dtype, t1, t2, t3))

    # Save output
    with open("output.txt", "w") as f:
        f.write("Size\tType\tInsertion\tMerge\tQuick\n")
        for r in results:
            f.write(f"{r[0]}\t{r[1]}\t{r[2]:.2f}\t{r[3]:.2f}\t{r[4]:.2f}\n")


if __name__ == "__main__":
    main()