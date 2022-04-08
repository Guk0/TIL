# https://www.acmicpc.net/problem/2775
# 부녀회장이 될테야

import sys

t = int(sys.stdin.readline())

for _ in range(t):
  k = int(sys.stdin.readline())
  n = int(sys.stdin.readline())

  arr = [i for i in range(1, 15)]
  for i in range(k):
    for j in range(1, n):
      arr[j] = arr[j - 1] + arr[j]
  print(arr[n-1])
