# https://www.acmicpc.net/problem/7576
# 토마토



from sys import stdin
from collections import deque


M, N = map(int, stdin.readline().split(" "))
arr = []
check_zero = False
queue = deque()
day = 0

for i in range(N):
  N_arr = list(map(int, stdin.readline().split(" ")))
  arr.append(N_arr)
  for index, j in enumerate(N_arr):
    if j == 0:
      check_zero = True
    elif j == 1:
      queue.append([index, i, 0])


def bfs():
  global day
  dx = [0, 0, 1, -1]
  dy = [1, -1, 0, 0]
  while queue:
    x, y, cnt = queue.popleft()
    if cnt > day:
      day = cnt

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < M and ny >= 0 and ny < N and arr[ny][nx] == 0:
        queue.append([nx, ny, cnt + 1])
        arr[ny][nx] = 1
  


if not check_zero:
  print(0)
else:
  check_finished = True
  bfs()

  for i in range(N):
    for j in range(M):
      if arr[i][j] == 0:
        check_finished = False

  if check_finished:
    print(day)
  else:
    print(-1)