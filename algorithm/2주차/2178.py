# https://www.acmicpc.net/problem/2178
# 미로탐색
# BFS


# DFS, BFS 상관 없이 풀어도 되는 유형 : 단순히 모든 끝점을 방문하는 것이 중요한 문제
# DFS로 풀어야 하는 유형
#   - 검색 대상 그래프가 큰 경우(정점과 간선의 개수가 많음) 
#   - 경로의 특징을 저장해둬야 하는 문제
#   - BFS는 경로의 특징을 가지지 못함
# BFS로 풀어야 하는 유형
#   - 최단거리 탐색
#   - BFS는 현재 노드에서 가까운 곳부터 찾기 때문에 경로 탐색 시 첫번째로 찾아지는 해답이 곧 최단거리.
#   - DFS는 처음 찾은 경로가 최단 거리가 아닐 가능성이 있음.
# 출처 : https://devyuseon.github.io/boj/boj-2178/


# BFS 풀이
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
queue = deque()

def bfs(x, y):
  queue.append([y, x, 1])
  visited[y][x] = True
  while True:
    n, m, depth = queue.popleft()
    if [n, m] == [N-1, M-1]:
      return depth    
    for i in [1, -1]:
      if m + i >= 0 and m + i < M and arr[n][m + i] == 1:
        if not visited[n][m+i]:
          queue.append([n, m+i, depth + 1])      
          visited[n][m+i] = True # append하는 시점에 True만들지 않으면 여러개가 append 될 수 있음.
      if n + i >= 0 and n + i < N and arr[n + i][m] == 1:
        if not visited[n+i][m]:
          queue.append([n + i, m, depth + 1])
          visited[n+i][m] = True
      

print(bfs(0, 0))

# DFS 풀이. 최단거리 탐색에 DFS는 적합하지 않음. 시간초과 뜰 가능성 매우 높음

# import sys

# N, M = map(int, sys.stdin.readline().split(" "))
# arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
# graph = [[] for _ in range(N)]
# visited = [[] for _ in range(N)]
# cnt = N * M

# for i in range(0, N):
#   for j in range(0, M):
#     graph[i].append([])
#     visited[i].append(False)
#     if arr[i][j] != 0:
#       if j + 1 < M and arr[i][j + 1] != 0:
#         graph[i][j].append([i, j+1])
#       if i + 1 < N and arr[i + 1][j] != 0:
#         graph[i][j].append([i + 1, j])
#       if j - 1 >= 0 and arr[i][j - 1] != 0:
#         graph[i][j].append([i, j - 1])
#       if i - 1 >= 0 and arr[i - 1][j] != 0:
#         graph[i][j].append([i - 1, j])


# def dfs(y, x, visited, depth):
#   global cnt
#   visited[y][x] = True
#   for el in graph[y][x]:
#     n, m = el
#     if el == [N-1, M-1] and depth + 1 < cnt:
#       cnt = depth + 1
#       break
#     if not visited[n][m]:
#       dfs(n, m, visited, depth+1)
#   visited[y][x] = False  # 갔던 길을 다시 초기화 해줘야함.


# dfs(0, 0, visited, 1)

# print(cnt)
