# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙 성공
# BFS


import sys

N, M = map(int, sys.stdin.readline().split(" "))
graph = [[] for _ in range((N+1))]
visited = [False]*(N+1)
result = [[] for _ in range((N+1))]
people = []

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split(" "))
  graph[a].append(b)
  graph[b].append(a)


def dfs(n, depth):
  visited[n] = True
  for i in graph[n]:
    if not visited[i] or (result[i] and min(result[i]) > depth + 1):
      result[i].append(depth+1)
      dfs(i, depth+1)


for i in range(1, N+1):
  result = [[] for _ in range((N+1))]
  visited = [False]*(N+1)
  dfs(i, 0)

  x = 0
  for el in result:
    if el:
      x += min(el)

  people.append(x)

print(people.index(min(people)) + 1)


# dfs로 풂.
# 최단 거리로 작성해야 하므로 visited를 체크하는 것 외에 (result[i] and min(result[i]) > depth + 1) 조건 추가.

# 다른 풀이들 보니 bfs로 많이 풂. 최단 거리 체크를 위해서는 bfs 써야할듯.
# bfs로 할 시 depth가 필요 없음. 이미 최초에 접근한 경로가 최단 depth임. 아래 코드 참조



# import sys
# from collections import deque


# N, M = map(int, sys.stdin.readline().split(" "))
# graph = [[] for _ in range((N+1))]
# people = []

# for _ in range(M):
#   a, b = map(int, sys.stdin.readline().split(" "))
#   graph[a].append(b)
#   graph[b].append(a)

# def bfs(n, result, visited):
#   visited[n] = True
#   queue = deque()
#   queue.append(n)

#   while queue:
#     a = queue.popleft()
#     for i in graph[a]:
#       if not visited[i]:
#         result[i] = result[a] + 1 # 이전 depth의 count 더해줌.
#         visited[i] = True
#         queue.append(i)


# for i in range(1, N+1):
#   result = [0] * (N+1)
#   visited = [False]*(N+1)
#   bfs(i, result, visited)

#   people.append(sum(result))

# print(people.index(min(people)) + 1)
