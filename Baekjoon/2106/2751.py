import sys

N = int(input())
num_list = []
tmp = [0 for _ in range(N)]
for _ in range(N):
    num_list.append(int(sys.stdin.readline().strip()))


def quick_sort():
    def sort(low, high):
        if low >= high:
            return
        mid = partition(low, high)
        sort(low, mid-1)
        sort(mid, high)

    def partition(low, high):
        pivot = num_list[(low+high)//2]

        while low <= high:
            while num_list[low] < pivot:
                low += 1
            while num_list[high] > pivot:
                high -= 1
            if low <= high:
                num_list[low], num_list[high] = num_list[high], num_list[low]
                low += 1
                high -= 1

        return low

    return sort(0, len(num_list)-1)


def merge_sort():
    def sort(left, right):
        if right - left < 2:
            return

        mid = (left + right) // 2
        sort(left, mid)
        sort(mid, right)
        merge(left, mid, right)

    def merge(left, mid, right):
        global tmp
        i, j = left, mid
        idx = 0

        while i < mid and j < right:
            if num_list[i] < num_list[j]:
                tmp[idx] = num_list[i]
                i += 1
                idx += 1
            else:
                tmp[idx] = num_list[j]
                j += 1
                idx += 1

        while i < mid:
            tmp[idx] = num_list[i]
            i += 1
            idx += 1

        while j < right:
            tmp[idx] = num_list[j]
            j += 1
            idx += 1

        for k in range(left, right):
            num_list[k] = tmp[k-left]

    sort(0, len(num_list))


merge_sort()
for x in num_list:
    sys.stdout.write(str(x) + '\n')