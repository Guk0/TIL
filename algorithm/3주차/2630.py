# https://www.acmicpc.net/problem/2630
# 색종이 만들기
# 재귀

import sys

N = int(sys.stdin.readline())
arr = []
result = [0, 0]

for _ in range(N):  
  arr.append(list(map(int, sys.stdin.readline().split(" "))))

def check(x, y, n):
  first = arr[y][x]
  for i in range(y, y+n):
    for j in range(x, x+n):
      if arr[i][j] != first:
        first = -1
        break

  if first == -1:
    n = int(n/2)
    check(x, y, n)
    check(x+n, y, n)
    check(x, y+n, n)
    check(x+n, y+n, n)
  else:
    result[first] += 1


check(0, 0, N)

for i in result:
  print(i)