# https://www.acmicpc.net/problem/14500
# 테트로미노
# 구현문제? dfs?

# 좌표 xy에 대해 사방으로 4칸씩 움직이다보면 중앙을 기준으로한 ㅗ와 중앙을 시작으로 한 ㅗ를 제외하고 모든 경우 탐색 가능.

from sys import stdin

N, M = map(int, stdin.readline().split())
graph = []
visited = [[False for _ in range(M)] for _ in range(N)]
result = 0

dx = [0, 1, 0, -1] # dfs 밖으로 빼는게 좋음.
dy = [1, 0, -1, 0]


for _ in range(N):
  graph.append(list(map(int, stdin.readline().split())))

max_number = max(map(max, graph))

def dfs(x, y, cnt, total):
  global result

  if result >= total + max_number * (4 - cnt): # 필수. 있고 없고 차이가 엄청 큼.
    return

  if cnt == 4:
    result = max(total, result)
    return

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
      if cnt == 2: # 옆으로 한칸 왔을때 다시 돌림. ㅗ를 위해서.
        visited[ny][nx] = True
        dfs(x, y, cnt + 1, total + graph[ny][nx])
        visited[ny][nx] = False

      visited[ny][nx] = True
      dfs(nx, ny, cnt + 1, total + graph[ny][nx])
      visited[ny][nx] = False

for i in range(N):
  for j in range(M):
    visited[i][j] = True # 루트 노드를 다시 방문하지 않도록.
    dfs(j, i, 1, graph[i][j])
    visited[i][j] = False

print(result)

# 기존 풀이. 좌표 xy에 대해 옆으로 3x2칸. 아래로 2x3칸 중 특정 좌표만 제외하면 stick을 제외한 나머지 도형들을 검사할 수 있음.
# stick은 따로 검사.

# from sys import stdin

# N, M = map(int, stdin.readline().split())
# graph = []
# result = 0

# for _ in range(N):
#   graph.append(list(map(int, stdin.readline().split())))

# def cnt_check(cnt):
#   global result
#   if cnt > result:
#     result = cnt

# def stick(x, y):
#   if x+3 < M:
#     cnt = sum([graph[y][x+i] for i in range(4)])  
#     cnt_check(cnt)
#   if y+3 < N:
#     cnt = sum([graph[y+i][x] for i in range(4)])
#     cnt_check(cnt)

# def hexa_logic(x, y, hexa_sum, is_horizontal):
#   arr = [0, 1]    
#   while arr != [5, 6]:
#     if not arr in [[1, 4], [0, 4], [1, 3], [1, 5], [2, 4]]:
#       tmp_sum = hexa_sum
#       for i in range(2):
#         if is_horizontal:
#           tmp_sum -= graph[y+arr[i] // 3][x+arr[i] % 3]  
#         else:
#           tmp_sum -= graph[y+arr[i] % 3][x+arr[i] // 3]
#       cnt_check(tmp_sum)

#     if arr[1] == 5:
#       arr = [arr[0]+1, arr[0]+2]
#     else:
#       arr = [arr[0], arr[1]+1]

# def hexa(x, y):
#   if x+3 < M and y + 1 < N: # 가로 직사각형(6개 타일)
#     hexa_sum = sum([graph[y][x], graph[y][x+1], graph[y][x+2], graph[y+1][x], graph[y+1][x+1], graph[y+1][x+2]])
#     hexa_logic(x, y, hexa_sum, True)
#   if y+3 < N and x + 1 < M: # 세로 직사각형(6개 타일)
#     hexa_sum = sum([graph[y][x], graph[y][x+1], graph[y+1][x], graph[y+1][x+1], graph[y+2][x], graph[y+2][x+1]])
#     hexa_logic(x, y, hexa_sum, False)

# for i in range(N):
#   for j in range(M):
#     stick(j, i)
#     hexa(j, i)


# print(result)