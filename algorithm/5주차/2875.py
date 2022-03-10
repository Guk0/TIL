# https://www.acmicpc.net/status?user_id=abcgy39&problem_id=2875&from_mine=1
# 대회 or 인턴

from sys import stdin

N, M, K = map(int, stdin.readline().split())
result = 0

while N >= 2 and M >= 1 and N+M >= K+3:
  N -= 2
  M -= 1
  result += 1


print(result)
  