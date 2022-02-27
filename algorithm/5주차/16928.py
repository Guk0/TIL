# https://www.acmicpc.net/problem/16928
# 뱀과 사다리 게임


# visited가 어찌보면 필요 없을 것 같지만 필수.
# 사다리와 뱀은 따로 관리하지 않고 같이 두고 관리.


from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split(" "))
ladder = []
ladder_start = []
visited = [False] * 101
queue = deque()
result = 0

for _ in range(N+M):
  x, y = map(int, stdin.readline().split(" "))
  ladder.append([x,y])
  ladder_start.append(x)  


def bfs():
  global result

  queue.append([1, 0])
  visited[1] = True
  while queue:
    x, cnt = queue.popleft()
    if x == 100:
      result = cnt
      break

    for i in range(1, 7):
      if x+i <= 100:
        if x+i in ladder_start and not visited[x+i]:
          index = ladder_start.index(x+i)
          visited[x+i] = True
          visited[ladder[index][1]] = True
          queue.append([ladder[index][1], cnt+1])
        else:
          if not visited[x+i]:
            visited[x+i] = True
            queue.append([x+i, cnt+1])

bfs()
print(result)