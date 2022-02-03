# https://www.acmicpc.net/problem/1764
# 듣보잡
# hash?

import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split(" "))
dic = {}
result = deque()

for _ in range(N):
  name = sys.stdin.readline().strip()
  dic[name] = 1


for _ in range(M):
  name = sys.stdin.readline().strip()
  try:
    dic[name]
    result.append(name)
  except KeyError:
    False


print(len(result))
for el in sorted(result):
  print(el)
