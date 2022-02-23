# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수

# test data
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

# graph : [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

from sys import stdin
from collections import deque


N, M = map(int, stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
queue = deque()
cnt = 0


for _ in range(M):
  x, y = map(int, stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs(x):
  global cnt
  queue.append(x)
  while queue:
    i = queue.popleft()
    for j in graph[i]:
      if not visited[j]:
        queue.append(j)
        visited[j] = True


for i in range(1, N+1):
  if not visited[i]:
    bfs(i)
    cnt += 1

print(cnt)



# from sys import stdin
# from collections import deque


# N, M = map(int, stdin.readline().split())
# graph = [[0 for _ in range(N)] for _ in range(N)]
# visited = [False for _ in range(N)]
# queue = deque()
# cnt = 0


# def bfs(x):
#   global cnt
#   queue.append(x)
#   result = False
#   while queue:
#     i = queue.pop()
#     visited[i] = True
#     for index, j in enumerate(graph[i]):
#       if graph[i][index] == 1 or graph[index][i] == 1:
#         result = True
#         queue.append(index)
#         graph[i][index] = 2
#         graph[index][i] = 2
#   if result:
#     cnt += 1

# for _ in range(M):
#   x, y = map(int, stdin.readline().split())
#   graph[x-1][y-1] = 1
#   graph[y-1][x-1] = 1

# for i in range(N):
#   if not visited[i]:
#     bfs(i)

# print(cnt)
