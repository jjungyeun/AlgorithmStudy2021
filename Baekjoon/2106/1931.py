import sys

N = int(input())
schedule = []
for _ in range(N):
    s, d = map(int, sys.stdin.readline().split())
    schedule.append((d, s))

schedule.sort()
end_time = 0
meeting_cnt = 0

for d, s in schedule:
    if s >= end_time:
        end_time = d
        meeting_cnt += 1

print(meeting_cnt)
