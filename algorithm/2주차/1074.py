# https://www.acmicpc.net/problem/1074
# Z
# 재귀

import sys

N, r, c = map(int, sys.stdin.readline().split(" "))


def check(n, y, x):
  if n == 0:
    return 0

  share = 2**(n-1)
  start = int(4**n / 4)

  if y < share:
    if x < share:
      start = 0
    else:
      x -= share
      start *= 1
  else:
    if x < share:
      y -= share
      start *= 2
    else:
      y -= share
      x -= share
      start *= 3

  return start + check(n-1, y, x)
  
print(check(N, r, c))
