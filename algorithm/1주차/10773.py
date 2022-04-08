# https://www.acmicpc.net/problem/10773
# 제로
# 스택

import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
  m = int(sys.stdin.readline())
  if m == 0:
    if len(arr) > 0:
      arr.pop()
  else:
    arr.append(m)

print(sum(arr))  