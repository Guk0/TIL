# https://www.acmicpc.net/problem/1003
# 피보나치 함수
# DP

# dictionary로 풂. 0과 1을 미리 할당해놓고 2부터 m까지 이전꺼를 계속 더해나감.

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