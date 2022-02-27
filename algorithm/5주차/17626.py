# https://www.acmicpc.net/problem/17626
# Four Squares
# dp, pypy3로 통과
# python3 로 통과하려면 어짜피 모든 자연수가 최대 4개의 제곱수로 표현 가능하므로 1~4의 경우의 수를 따져 풀면 됨.

from sys import stdin

N = int(stdin.readline())
arr = [0 for _ in range(N+1)]
arr[1] = 1


for i in range(2, N+1):
  j = 1
  arr[i] = float("inf")
  while j ** 2 <= i:
    arr[i] = min(arr[i], arr[i - (j ** 2)] + 1) # 제곱한 수가 i와 동일하면 0
    j += 1

print(arr[N])
