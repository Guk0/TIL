# https://www.acmicpc.net/problem/1992
# 쿼드트리
# 1780이랑 비슷하게 풀어야 할듯.


import sys

N = int(sys.stdin.readline())
arr = []
ans = ""
for _ in range(N):
  arr.append(list(map(int, sys.stdin.readline().strip())))

def check(x, y, n):
  global ans
  result = arr[y][x]
  for i in range(y, y + n):
    for j in range(x, x + n):
      if result != arr[i][j]:
        result = -1

  if result == -1:
    n = int(n/2)
    ans += "("
    check(x, y, n)
    check(x + n, y, n)
    check(x, y + n, n)
    check(x + n, y + n, n)
    ans += ")"
  else:
    ans += str(result)


check(0, 0, N)

print(ans)