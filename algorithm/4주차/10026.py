# https://www.acmicpc.net/problem/10026
# 적록색약


# [[False] * N] * N으로 만든 2차원 list는 서로 참조하게 되어 있음.
# RGB_visitied[0][0] = True 시 RGB_visitied[0~4][0] 모두 True로 바뀜

from sys import stdin
from collections import deque

N = int(stdin.readline())
RGB_visitied = [[False] * N for _ in range(N)]
RB_visitied = [[False] * N for _ in range(N)]

arr = []
queue = deque()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for _ in range(N):
  arr.append(list(stdin.readline().strip()))

def search(i, j, is_RGB):
  queue.append([i, j, arr[i][j]])
  if is_RGB:
    RGB_visitied[i][j] = True
  else:
    RB_visitied[i][j] = True

  count = 0
  while queue:    
    y, x, color = queue.pop()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if is_RGB:
        if 0 <= nx < N and 0 <= ny < N and not RGB_visitied[ny][nx] and color == arr[ny][nx]:
          count += 1
          queue.append([ny, nx, arr[ny][nx]])
          RGB_visitied[ny][nx] = True

      else:
        if 0 <= nx < N and 0 <= ny < N and not RB_visitied[ny][nx]:
          if color == arr[ny][nx] or (color == "G" and arr[ny][nx] == "R") or  (color == "R" and arr[ny][nx] == "G"):
            count += 1
            queue.append([ny, nx, arr[ny][nx]])
            RB_visitied[ny][nx] = True

  return count


RGB = 0
RB = 0

for i in range(N):
  for j in range(N):
    if not RGB_visitied[i][j] and search(i, j, True) >= 0:
      RGB += 1
    if not RB_visitied[i][j] and search(i, j, False) >= 0:
      RB += 1

print(RGB, RB)