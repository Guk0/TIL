# https://www.acmicpc.net/problem/2606
# 바이러스
# dfs

import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
visitied = [False] * (N+1)
cnt = 0

for _ in range(M):
  X, Y = map(int, sys.stdin.readline().split(" "))
  graph[X].append(Y)
  graph[Y].append(X)


def dfs(x):
  global cnt

  visitied[x] = True
  for i in graph[x]:
    if not visitied[i]:
      cnt += 1
      dfs(i)


dfs(1)
print(cnt)