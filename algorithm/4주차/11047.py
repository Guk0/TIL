# https://www.acmicpc.net/problem/11047
# 동전 0
# 그리디 알고리즘

from sys import stdin
from collections import deque

N, K = map(int, stdin.readline().split(" "))
queue = deque()
cnt = 0


for _ in range(N):
  queue.appendleft(int(stdin.readline().strip()))


for i in queue:
  if K // i > 0:
    cnt += K // i
    K = K % i

print(cnt)
