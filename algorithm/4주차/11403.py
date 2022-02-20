# https://www.acmicpc.net/problem/11403
# 경로 찾기
# 플로이드-워셜 알고리즘


# 플로이드-워셜 vs 다익스트라 vs 벨만포드

# 다익스트라 : 하나의 정점에서 다른 모든 정점까지의 최단거리
#   - https://techblog-history-younghunjo1.tistory.com/247
# 플로이드 워셜 : 모든 노드 간 최단 경로. 음의 간선도 사용할 수 있음.
#   - https://it-garden.tistory.com/247
# 벨만 포드 : 하나의 정점에서 다른 모든 정점까지의 최단거리. 음의 간선 활용 가능. 
#           음수 사이클이 존재하는 경우를 피해 최단 거리를 계산할 수 있음.
#   - https://techblog-history-younghunjo1.tistory.com/247


from sys import stdin

N = int(stdin.readline())
graph = []

for _ in range(N):
  graph.append(list(map(int, stdin.readline().split(" "))))


for k in range(N):
  for i in range(N):
    for j in range(N):
      if graph[i][k] == 1 and graph[k][j] == 1:
        graph[i][j] = 1

for i in range(N):
  print(" ".join(map(str, graph[i])))




# from sys import stdin

# N = int(stdin.readline())
# graph = []
# result = [[0 for _ in range(N)] for _ in range(N)]

# for _ in range(N):
#   graph.append(list(map(int, stdin.readline().strip().split(" "))))

# def search(x, y, arr):
#   for index, el in enumerate(graph[y]):
#     if el == 1 and result[y][index] == 0:
#       result[y][index] = 1
#       search(y, index, [*arr, x, y])
#       for j in [*arr]:
#         result[j][index] = 1

# for i in range(N):
#   for j in range(N):
#     if result[i][j] == 0:
#       search(j, i, [])

# print(result)