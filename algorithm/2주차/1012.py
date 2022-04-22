# https://www.acmicpc.net/problem/1012
# 유기농배추
# DFS

from sys import stdin
from collections import deque

input = stdin.readline

T = int(input())

for _ in range(T):
  M, N, K = map(int, input().split())
  visited = [[False for _ in range(M)] for _ in range(N)]
  arr = [list(map(int, input().split())) for _ in range(K)]
  stack = deque()
  answer = 0

  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]

  for el in arr:
    stack.append([*el, 0])

  while stack:
    x, y, cnt = stack.pop()        
    if not visited[y][x]:      
      visited[y][x] = True
      if cnt == 0:
        answer += 1
        cnt = 1        

      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if [nx, ny] in arr and 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
          stack.append([nx, ny, cnt])

  print(answer)



# DFS 로 개선하기 전

import sys
sys.setrecursionlimit(9999)


T = int(sys.stdin.readline())
result = []

for _ in range(T):
  M, N, K = map(int, sys.stdin.readline().split())
  arr = []
  cnt = 0
  result = []

  def search(el):
    tmp = [[el[0] + 1, el[1]], [el[0], el[1] + 1], [el[0] - 1, el[1]], [el[0], el[1] - 1]]
    for tmp_el in tmp:
      if tmp_el in arr and not tmp_el in result:
        result.append(tmp_el)
        search(tmp_el)        

  for _ in range(K):
    X, Y = map(int, sys.stdin.readline().split())
    arr.append([X, Y])
  
  arr.sort()

  for el in arr:
    if not el in result:
      cnt += 1
      result.append(el)
      search(el)



  print(cnt)
