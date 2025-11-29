class PancakeSorter:
    def __init__(self):
        pass

    def flip(self, arr, k):
        """Переворачивает часть массива до индекса k."""
        start = 0
        while start < k:
            arr[start], arr[k] = arr[k], arr[start]
            start += 1
            k -= 1

    def sort(self, arr):
        """Основной метод сортировки Pancake sort."""
        n = len(arr)
        for curr_size in range(n, 1, -1):
            max_idx = 0
            for i in range(1, curr_size):
                if arr[i] > arr[max_idx]:
                    max_idx = i
            if max_idx != curr_size - 1:
                self.flip(arr, max_idx)
                self.flip(arr, curr_size - 1)
        return arr