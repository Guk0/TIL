# https://www.acmicpc.net/problem/1697
# 숨바꼭질
# BFS

# +1, -1, *2 씩 움직일 수 있음.
# N > M 일때는 -1 씩 밖에 못 움직임.
# N < M 일때는 M-N을하여 1부터 M-N까지 최단거리로 구함.
# 시작 혹은 끝점이 고정이 아니다.

# DP라 생각했으나 BFS
# dic 정의하고 풀었으나 시간초과.
# v-1인 경우 음수 끝까지 내려가버림. 조건을 >= 0 을 추가했으면 시간초과 안되고 통과했을듯.

from collections import deque

N, M = map(int, input().split(" "))
queue = deque([[N, 0]])
visited = [False] * 100001

while queue:
  v, depth = queue.popleft()
  visited[v] = True
  if v == M:
    break
  else:
    if v-1 >= 0 and not visited[v-1]:
      queue.append([v-1, depth + 1])
    if v+1 <= 100000 and not visited[v+1]:
      queue.append([v+1, depth + 1])
    if v*2 <= 100000 and not visited[v*2]:
      queue.append([v*2, depth + 1])

if N != M:
  if N > M:
    print(N - M)
  else:
    print(depth)
else:
  print(0)
    
  



# DP로 시도했던 코드

# N, M = map(int, input().split(" "))

# dic = {1: 0, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 3, 9: 4, 10: 4}

# if M-N <= 0:
#   print(abs(M-N))
# elif M-N < 11:
#   print(dic[M-N])
# else:
#   for i in range(11, M-N+1):
#     cnt = dic[i-1]
#     if i % 2 == 0 and dic[i/2] < cnt:
#       cnt = dic[i/2]
#     if (i + 1) % 2 == 0 and dic[(i + 1) / 2] + 1 < cnt:
#       cnt = dic[(i + 1) / 2] + 1
#     dic[i] = cnt + 1

#   print(dic[M-N])

