# https://www.acmicpc.net/problem/7662
# 이중 우선순위 큐


import heapq
from sys import stdin

N = int(stdin.readline())


for _ in range(N):
  M = int(stdin.readline())
  visited = [False] * 1000001

  ascQueue = []
  descQueue = []

  for i in range(M):
    operator, number = map(str, stdin.readline().strip().split())

    if operator == "I":
      heapq.heappush(ascQueue, [int(number), i])
      heapq.heappush(descQueue, [int(number) * -1, i])

    else:
      if int(number) == -1:
        while ascQueue and visited[ascQueue[0][1]]:
          heapq.heappop(ascQueue)
          
        if ascQueue:
          poped = heapq.heappop(ascQueue)
          visited[poped[1]] = True

      else:
        while descQueue and visited[descQueue[0][1]]:
          heapq.heappop(descQueue)
        
        if descQueue:
          poped = heapq.heappop(descQueue)
          visited[poped[1]] = True
          
  while descQueue and visited[descQueue[0][1]]:
    heapq.heappop(descQueue)

  while ascQueue and visited[ascQueue[0][1]]:
    heapq.heappop(ascQueue)

  if ascQueue and descQueue:
    print(descQueue[0][0] * -1, ascQueue[0][0])
  else:
    print("EMPTY")