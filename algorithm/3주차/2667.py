# https://www.acmicpc.net/problem/2667
# 단지번호붙이기


# visited를 없애고 방문한 좌표를 0으로 바꿔주면 잘 됨.
# 문제가 좀 이상한듯. 좌우 상하에 다른 집이 있어야 단지인데 주위에 집이 없는 곳도 단지로 제출해야 통과함.

import sys

N = int(sys.stdin.readline())
arr = []
cnt_list = [] # 단지당 가구수

for _ in range(N):
  arr.append(list(map(int, sys.stdin.readline().strip())))


def check(y, x, index):
  arr[y][x] = 0

  for i in [1, -1]:
    if x + i >= 0 and x + i < N and arr[y][x+i] == 1:
      cnt_list[index] += 1
      check(y, x+i, index)
    if y + i >= 0 and y + i < N and arr[y+i][x] == 1:
      cnt_list[index] += 1
      check(y+i, x, index)

for i in range(N):
  for j in range(N):
    if arr[i][j] == 1:
      cnt_list.append(1)
      check(i, j, len(cnt_list)-1)



cnt_list.sort()
print(len(cnt_list))

for i in cnt_list:
  print(i)


# import sys

# N = int(sys.stdin.readline())
# arr = []
# visited = [[False] * N] * N
# result = [] # 단지당 가구수

# for _ in range(N):
#   arr.append(list(map(int, sys.stdin.readline().strip())))


# def check(y, x, index):
#   visited[y][x] = True

#   for i in [1, -1]:
#     if x + i >= 0 and x + i < N and arr[y][x+i] == 1 and not visited[y][x+i]:
#       result[index] += 1
#       check(y, x+i, index)
#     if y + i >= 0 and y + i < N and arr[y+i][x] == 1 and not visited[y+i][x]:
#       result[index] += 1
#       check(y+i, x, index)

# for i in range(N):
#   for j in range(N):
#     if arr[i][j] == 1 and not visited[i][j]:
#       result.append(1)
#       check(i, j, len(result)-1)


# a = sorted(list(set(result)))
# a.pop(0)
# print(len(a))
# for el in a:
#   print(el)



# 7
# 0110101
# 0110100
# 1100100
# 0000111
# 0100000
# 0111110
# 0111001