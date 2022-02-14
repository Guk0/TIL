# https://www.acmicpc.net/problem/7569
# 토마토
# bfs

# [h][n][m] 일때 [h+1][n][m], [h-i][n][m], [h][n+1][m], [h][n-1][m], [h][n][m+1], [h][n][m-1]


from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().split(" "))
arr = []
queue = deque()
cnt = 0
result = False

for i in range(H):
  arr.append([])
  for j in range(N):
    m = list(map(int, stdin.readline().split(" ")))
    arr[i].append(m)
    for index, k in enumerate(m):
      if k == 1:
        queue.append([index, j, i, 0])
      if k == 0:
        result = True


def bfs():
  global cnt
  while queue:
    x, y, h, depth = queue.popleft()
    if depth > cnt:
      cnt = depth
    dx = [0, 0, 0, 0, 1, -1]
    dy = [0, 0, 1, -1, 0, 0]
    dh = [1, -1, 0, 0, 0, 0]
    for i in range(6):
      nx = x + dx[i]
      ny = y + dy[i]
      nh = h + dh[i]
      if nx >= 0 and nx < M and ny >= 0 and ny < N and nh >= 0 and nh < H and arr[nh][ny][nx] == 0:
        arr[nh][ny][nx] = 1
        queue.append([nx, ny, nh, depth + 1])


if result:
  bfs()
  not_rotten = False
  for i in arr:
    for j in i:
      for k in j:
        if k == 0:
          not_rotten = True
  
  if not_rotten:
    print(-1)
  else:
    print(cnt)
else:
  print(0)

#  0 -1 0 0 0
# -1 -1 0 1 1
#  0  0 0 1 1
