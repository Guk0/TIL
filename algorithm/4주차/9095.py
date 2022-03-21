# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기
# dp


# top down 방식
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


# https://www.acmicpc.net/problem/15988
# 1, 2, 3 더하기 3

# bottom up 방식

# from sys import stdin

# T = int(stdin.readline())

# dp = [0 for _ in range(1000000)]
# dp[0], dp[1], dp[2] = 1, 2, 4

# for i in range(3, 1000000):
#   dp[i] = dp[i-1] % 1000000009 + dp[i-2] % 1000000009 + dp[i-3] % 1000000009

# for _ in range(T):
#   n = int(stdin.readline().strip())
#   print(dp[n-1] % 1000000009)