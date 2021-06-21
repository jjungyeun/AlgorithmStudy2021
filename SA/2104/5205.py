def swap(i, j, arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]
    arr = swap(0, len(arr)//2, arr)
    i, j = 1, len(arr)-1
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr = swap(i, j, arr)
    arr = swap(0, j, arr)

    left = quick_sort(arr[:j])
    right = quick_sort(arr[i:])

    return left + [pivot] + right


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        N = int(input())
        num_list = list(map(int, input().split()))
        res = quick_sort(num_list)
        # print(res)
        print("#%d %d" % (T, res[int(N/2)]))