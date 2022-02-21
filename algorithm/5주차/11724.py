# # https://www.acmicpc.net/problem/11724
# # 연결 요소의 개수


# from sys import stdin
# from collections import deque


# N, M = map(int, stdin.readline().split())
# graph = [[0 for _ in range(N)] for _ in range(N)]

# queue = deque()
# cnt = 0


# def bfs(y, x):
#   global cnt  
#   queue.append([y, x])
#   graph[y][x] = 2
#   graph[x][y] = 2
#   cnt += 1
#   while queue:
#     i, j = queue.pop()
#     for k in graph[i]:
#       if graph[i][k] == 1:
#         queue.append([k, i])
#         graph[i][k] = 2
#         graph[k][i] = 2


# for _ in range(M):
#   x, y = map(int, stdin.readline().split())
#   graph[x-1][y-1] = 1
#   graph[y-1][x-1] = 1

# print(graph)

# for i in range(N):
#   for j in range(N):
#     if graph[i][j] == 1:
#       bfs(j, i)

# print(cnt)
