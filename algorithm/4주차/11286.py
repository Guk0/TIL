# https://www.acmicpc.net/problem/11286
# 절댓값 힙


import heapq
from sys import stdin


N = int(stdin.readline())
heap = []

for _ in range(N):
  M = int(stdin.readline())
  if M == 0:
    if len(heap) > 0:
      print(heapq.heappop(heap)[1])
    else:
      print(0)
  else:
    heapq.heappush(heap, [abs(M), M])
