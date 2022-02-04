# https://www.acmicpc.net/problem/1931
# 회의실 배정


# 1 3, 1 4가 있을 때 1 3, 3 10 와 1 4, 4 5, 5 6 으로 선택이 갈릴 거라 생각함.
# 근데 끝나는 시간을 빠른 걸로 찾으면 1 3, 4 5, 5 6 으로 갈거니까 잘 못된 생각이었음.

import sys


N = int(sys.stdin.readline())
arr = []

for _ in range(N):
  arr.append(list(map(int, sys.stdin.readline().split(" "))))

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end_time = arr[0][1]

for i in range(1, N):
  if end_time <= arr[i][0]:
    cnt += 1
    end_time = arr[i][1]

print(cnt)