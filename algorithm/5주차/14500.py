# https://www.acmicpc.net/problem/14500
# 테트로미노
# 구현문제


from sys import stdin

N, M = map(int, stdin.readline().split())
graph = []
result = 0

for _ in range(N):
  graph.append(list(map(int, stdin.readline().split())))

def cnt_check(cnt):
  global result
  if cnt > result:
    result = cnt

def stick(x, y):
  if x+3 < M:
    cnt = sum([graph[y][x+i] for i in range(4)])  
    cnt_check(cnt)
  if y+3 < N:
    cnt = sum([graph[y+i][x] for i in range(4)])
    cnt_check(cnt)

def square(x, y):
  if x+1 < M and y + 1 < N:
    nx = [0, 0, 1, 1]
    ny = [0, 1, 0, 1]
    cnt = sum([graph[y+ny[i]][x+nx[i]] for i in range(4)])
    cnt_check(cnt) 

def hexa_logic(x, y, hexa_sum, is_horizontal):
  arr = [0, 1]    
  while arr != [5, 6]:
    if not arr in [[1, 4], [0, 4], [1, 3], [1, 5], [2, 4]]:
      tmp_sum = hexa_sum
      for i in range(2):
        if is_horizontal:
          tmp_sum -= graph[y+arr[i] // 3][x+arr[i] % 3]  
        else:
          tmp_sum -= graph[y+arr[i] % 3][x+arr[i] // 3]
      cnt_check(tmp_sum)

    if arr[1] == 5:
      arr = [arr[0]+1, arr[0]+2]
    else:
      arr = [arr[0], arr[1]+1]

def hexa(x, y):
  if x+3 < M and y + 1 < N: # 가로 직사각형(6개 타일)
    hexa_sum = sum([graph[y][x], graph[y][x+1], graph[y][x+2], graph[y+1][x], graph[y+1][x+1], graph[y+1][x+2]])
    hexa_logic(x, y, hexa_sum, True)
  if y+3 < N and x + 1 < M: # 세로 직사각형(6개 타일)
    hexa_sum = sum([graph[y][x], graph[y][x+1], graph[y+1][x], graph[y+1][x+1], graph[y+2][x], graph[y+2][x+1]])
    hexa_logic(x, y, hexa_sum, False)

def check(x, y):
  stick(x, y)
  square(x, y)
  hexa(x, y)


for i in range(N):
  for j in range(M):
    check(j, i)

print(result)