# https://www.acmicpc.net/problem/7569
# 토마토


from sys import stdin

M, N, H = map(int, stdin.readline().split(" "))

arr = []

for i in range(H):
  arr.append([])
  for _ in range(N):
    arr[i].append(list(map(int, stdin.readline().split(" "))))




print(arr)


#  0 -1 0 0 0
# -1 -1 0 1 1
#  0  0 0 1 1
