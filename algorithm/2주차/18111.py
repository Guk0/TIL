import sys

N, M, B = map(int, sys.stdin.readline().split(" "))
arr = []
inventory = B
cnt = 0

for _ in range(N):
  arr = list(map(int, sys.stdin.readline().split(" ")))

for target in range(257):
  for i in arr:
    for j in arr[i]:
      if j < target:
        cnt += 1
      elif j > target:
        cnt += 2
        inventory += 1



# brute force.
# 최대 높이가 256인 것을 보면 0~256까지 돌면서 모든 경우의 수를 탐색 가능.
