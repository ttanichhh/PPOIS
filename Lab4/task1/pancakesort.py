def flip(arr, k):
    start = 0
    while start < k:
        arr[start], arr[k] = arr[k], arr[start]
        start += 1
        k -= 1

def pancake_sort(arr):
    n = len(arr)
    for curr_size in range(n, 1, -1):
        max_idx = 0
        for i in range(1, curr_size):
            if arr[i] > arr[max_idx]:
                max_idx = i
        if max_idx != curr_size - 1:
            flip(arr, max_idx)
            flip(arr, curr_size - 1)
    return arr
