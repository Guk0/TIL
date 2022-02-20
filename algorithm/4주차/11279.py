# https://www.acmicpc.net/problem/11279
# 최대힙

# 값에 -1을 곱하여 최대힙 구현

import sys
import heapq

N = int(sys.stdin.readline())
heap = []


for _ in range(N):
  M = int(sys.stdin.readline())
  if M == 0:
    if len(heap) > 0:
      print(heapq.heappop(heap) * -1)
    else:
      print(0)
  else:
    heapq.heappush(heap, M*-1)  


