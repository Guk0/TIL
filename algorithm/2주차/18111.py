# https://www.acmicpc.net/problem/18111
# 마인크래프트
# Brute Force
# 최대 높이가 256인 것을 보면 0~256까지 돌면서 모든 경우의 수를 탐색 가능.

import sys

N, M, B = map(int, sys.stdin.readline().split(" "))
arr = []
min_cnt = "Not Assigned"
max_floor = 0

for _ in range(N):
  arr.append(list(map(int, sys.stdin.readline().split(" "))))

for target in range(257):
  inventory = B
  cnt = 0  
  for el in arr:
    for j in el:
      if j < target:
        cnt += target - j
        inventory -= target - j
      else:
        cnt += (j - target)*2
        inventory += j - target

  if inventory < 0:
    continue

  if min_cnt == "Not Assigned" or min_cnt >= cnt:
    min_cnt = cnt
    max_floor = target

print(min_cnt, max_floor)
