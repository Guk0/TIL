# https://www.acmicpc.net/problem/1003
# 피보나치 함수
# DP


from sys import stdin

N = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(N)]
dp = [0] * (max(arr)+1)
dp[0], dp[1], dp[2] = 0, 1, 1

for i in range(3, max(arr)+1):
  dp[i] = dp[i-1] + dp[i-2]

for i in arr:
  if i == 0:
    print(1, 0)
  else:
    print(dp[i-1], dp[i])



# dictionary로 풂. 0과 1을 미리 할당해놓고 2부터 m까지 이전꺼를 계속 더해나감.
# 개선하기 전 풀이

import sys

n = int(sys.stdin.readline())
dic = {0: [1, 0], 1: [0, 1]}

for _ in range(n):
  m = int(sys.stdin.readline())
  
  for i in range(2, m+1):
    dic[i] = [0,0]
    dic[i][0] = dic[i-1][0] + dic[i-2][0]
    dic[i][1] = dic[i-1][1] + dic[i-2][1]

  print(dic[m][0], dic[m][1])