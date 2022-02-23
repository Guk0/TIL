# https://www.acmicpc.net/problem/11727
# 2xn 타일링 2

# DP
# 11726번과 동일한 문제. (n-2번 경우의 수)*2 + (n-1번의 경우의 수)를 하면 된다.
# 가로 2개와 사각형 두 경우의 수가 있기 때문에 *2를 함.


# dict
# 1 1
# 2 3
# 3 5
# 4 11
# 5 21
# 6 43
# 7 85
# 8 171


from sys import stdin

N = int(stdin.readline())
dic = {1: 1, 2: 3}


if N > 2:
  for i in range(3, N+1):
    dic[i] = dic[i-1] + (dic[i-2] * 2)
  print(dic[N]%10007)
else:
  print(dic[N])