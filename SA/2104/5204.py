def merge(list1, list2):
    if list1[-1] > list2[-1]:
        global cnt
        cnt += 1

    len1, len2 = len(list1), len(list2)
    res = [0] * (len1 + len2)
    i, j = 0, 0
    pointer = 0
    while i < len1 and j < len2:
        if list1[i] > list2[j]:
            res[pointer] = list2[j]
            j += 1
        else:
            res[pointer] = list1[i]
            i += 1
        pointer += 1

    while i < len1:
        res[pointer] = list1[i]
        i += 1
        pointer += 1
    while j < len2:
        res[pointer] = list2[j]
        j += 1
        pointer += 1
    return res


def merge_sort(num_list):
    length = len(num_list)

    if length == 1:
        return num_list

    mid = length // 2
    left = merge_sort(num_list[:mid])
    right = merge_sort(num_list[mid:])
    res = merge(left, right)

    return res


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):
        N = int(input())
        cnt = 0
        tmp = map(int, input().split())
        num_list = [x for x in tmp]
        res= merge_sort(num_list)

        print("#%d %d %d" % (T, res[N//2], cnt))