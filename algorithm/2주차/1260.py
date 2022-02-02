# https://www.acmicpc.net/problem/1260
# DFS와 BFS
# DFS, BFS


import sys

N, M, V = map(int, sys.stdin.readline().split(" "))
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
queue = []

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, N+1):
  graph[i].sort()


def dfs(n):
  print(n, end=" ")
  visited[n] = True
  for i in graph[n]:
    if not visited[i]:
      dfs(i)

def bfs(n):
  visited[n] = True
  queue.append(n)
  while queue:
    popped = queue.pop(0)    
    print(popped, end=" ")
    for j in graph[popped]:
      if not visited[j]:
        queue.append(j)
        visited[j] = True
        

dfs(V)
print()

visited = [False] * (N + 1)

bfs(V)



# 그래프 생성 하는 방법, 생성 후  bfs, dfs 적용하는 방법에 대한 숙지가 필요.
# https://goplanit.site/42.%20Algorithm(1260_py)/