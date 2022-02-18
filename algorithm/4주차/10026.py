# https://www.acmicpc.net/problem/10026
# 적록색약

# from sys import stdin
# from collections import deque

# N = int(stdin.readline())
# visitied = [[False] * N] * N
# arr = []
# queue = deque()

# for _ in range(N):
#   arr.append(list(stdin.readline().strip()))

# def search():
#   queue.append([0, 0, arr[0][0]])
#   nx = [0, 0, 1, -1]
#   ny = [1, -1, 0, 0]
#   while queue:
#     y, x, color = queue.pop()
#     visitied[y][x] = True
#     for i in range(4):
#       dx = x + nx[i]
#       dy = y + ny[i]
#       if not visitied[dy][dx] and dx >= 0 and dx < N and dy >= 0 and dy < N and color == arr[dy][dx]:

