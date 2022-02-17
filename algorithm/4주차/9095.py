# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기

from sys import stdin

N = int(stdin.readline())

def minus(x):
  global count
  if x == 0:
    count += 1
    return
  
  if x > 0:
    minus(x-1)
  if x > 1:
    minus(x-2)
  if x > 2:
    minus(x-3)

for _ in range(N):
  x = int(stdin.readline())
  count = 0
  minus(x)
  print(count)
