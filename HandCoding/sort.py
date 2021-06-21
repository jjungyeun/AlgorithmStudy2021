def insertion_sort(arr):
    for i in range(1, len(arr)):
        j, key = i - 1, arr[i]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = parition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def parition(low, high):
        pivot = arr[(low + high) // 2]

        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1

        return low

    sort(0, len(arr) - 1)


def merge_sort(arr):
    def sort(left, right):
        if right - left < 2:
            return

        mid = (left + right) // 2
        sort(left, mid)
        sort(mid, right)
        merge(left, mid, right)

    def merge(left, mid, right):
        i, j = left, mid
        temp = []
        while i < mid and j < right:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1

        while i < mid:
            temp.append(arr[i])
            i += 1

        while j < right:
            temp.append(arr[j])
            j += 1

        for k in range(left, right):
            arr[k] = temp[k - left]

    sort(0, len(arr))


sample = [5,7,2,4,9,3]
insertion_sort(sample)
print("insertion_sort: ",sample)

sample = [5,7,2,4,9,3]
selection_sort(sample)
print("selection_sort: ",sample)

sample = [5,7,2,4,9,3]
bubble_sort(sample)
print("bubble_sort: ",sample)

sample = [5,7,2,4,9,3]
quick_sort(sample)
print("quick_sort: ",sample)

sample = [5,7,2,4,9,3]
merge_sort(sample)
print("merge_sort: ",sample)
