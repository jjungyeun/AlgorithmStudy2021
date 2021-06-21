
def getMostTask(task_list):
    available_task = 0
    last_end = 0
    for tup in task_list:
        start_time, end_time = tup
        if start_time < last_end:
            continue
        available_task += 1
        last_end = end_time

    return available_task


if __name__ == '__main__':
    TC = int(input())
    for T in range(1, TC + 1):

        N = int(input())
        task_list = []
        for i in range(N):
            a, b = map(int, input().split(' '))
            task_list.append((a,b))

        task_list = sorted(task_list, key=lambda item:item[1])
        res = getMostTask(task_list)
        print("#%d %d" % (T, res))