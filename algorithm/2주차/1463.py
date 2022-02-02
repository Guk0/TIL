# https://www.acmicpc.net/problem/1463
# 1로 만들기

import sys


n = int(sys.stdin.readline())
count = 0


while n != 0:
  count += 1
  if n % 3 == 0:
    n = n/3
  elif n % 2 == 0:
    n = n/2
  else:
    n -= 1

print(count)