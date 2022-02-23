# https://www.acmicpc.net/problem/11726
# 2xn 타일링

# DP
# 첫번째에 - 을 놓느냐 |를 놓느냐 2가지 경우의 수. -을 놓는 경우 n-2의 경우의 수와 동일. |를 놓는 경우 n-1의 경우의 수와 동일

# 1 1
# 2 2
# 3 3
# 4 5
# 5 8
# 6 13
# 7 21
# 8 34
# 9 55

from sys import stdin

N = int(stdin.readline())
dic = {1: 1, 2: 2}


if N > 2:
  for i in range(3, N+1):
    dic[i] = dic[i-1] + dic[i-2]
  print(dic[N]%10007)
else:
  print(dic[N])