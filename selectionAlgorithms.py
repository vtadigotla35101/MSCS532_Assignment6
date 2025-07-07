import random
import sys
import time

# Set a higher recursion limit for handling larger arrays
sys.setrecursionlimit(30000)

# --- Randomized Selection (Quickselect) ---

def randomized_select(arr, k):
    """
    Finds the k-th smallest element in an array in expected linear time.
    k is 1-based index (e.g., k=1 for smallest, k=n for largest).
    """
    if not (1 <= k <= len(arr)):
        raise ValueError("k is out of the bounds of the array")
    
    # Work on a copy to not modify the original array
    arr_copy = list(arr)
    return _randomized_select_helper(arr_copy, 0, len(arr_copy) - 1, k - 1)

def _randomized_select_helper(arr, low, high, i):
    """Recursive helper for Randomized Quickselect."""
    while low <= high:
        # Base case: if the partition has one element
        if low == high:
            return arr[low]

        # Partition the array and get the pivot's final index
        pivot_index = _randomized_partition(arr, low, high)

        if i == pivot_index:
            return arr[i]
        elif i < pivot_index:
            high = pivot_index - 1
        else:
            low = pivot_index + 1

def _randomized_partition(arr, low, high):
    """Partitions the array using a random pivot."""
    rand_pivot_idx = random.randint(low, high)
    arr[rand_pivot_idx], arr[high] = arr[high], arr[rand_pivot_idx]
    return _partition(arr, low, high)

def _partition(arr, low, high):
    """Lomuto partition scheme using the last element as pivot."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# --- Deterministic Selection (Median of Medians) ---

def deterministic_select(arr, k):
    """
    Finds the k-th smallest element in worst-case linear time.
    k is 1-based index.
    """
    if not (1 <= k <= len(arr)):
        raise ValueError("k is out of the bounds of the array")
    
    arr_copy = list(arr)
    return _median_of_medians_select(arr_copy, 0, len(arr_copy) - 1, k)

def _median_of_medians_select(arr, low, high, k):
    """Recursive helper for the Median of Medians algorithm."""
    # If the partition has 5 or fewer elements, sort and return
    if high - low + 1 <= 5:
        sub_arr = sorted(arr[low:high+1])
        return sub_arr[k-1]

    # 1. Divide the array into groups of 5
    medians = []
    for i in range(low, high + 1, 5):
        chunk_end = min(i + 4, high)
        chunk = arr[i:chunk_end+1]
        chunk.sort()
        medians.append(chunk[len(chunk) // 2])

    # 2. Find the median of the medians recursively
    median_of_medians = _median_of_medians_select(medians, 0, len(medians) - 1, (len(medians) + 1) // 2)

    # 3. Partition the array around the median of medians
    pivot_index = _partition_around_pivot(arr, low, high, median_of_medians)
    
    # The rank of the pivot
    rank = pivot_index - low + 1

    # 4. Recurse into the correct partition
    if k == rank:
        return arr[pivot_index]
    elif k < rank:
        return _median_of_medians_select(arr, low, pivot_index - 1, k)
    else:
        return _median_of_medians_select(arr, pivot_index + 1, high, k - rank)

def _partition_around_pivot(arr, low, high, pivot_val):
    """Partitions the array around a specific pivot value."""
    # Find the pivot value in the array and move it to the end
    for i in range(low, high + 1):
        if arr[i] == pivot_val:
            arr[i], arr[high] = arr[high], arr[i]
            break
    # Use standard Lomuto partition
    return _partition(arr, low, high)