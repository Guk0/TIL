import sys
sys.setrecursionlimit(9999)


T = int(sys.stdin.readline())
result = []

for _ in range(T):
  M, N, K = map(int, sys.stdin.readline().split())
  arr = []
  cnt = 0
  result = []

  def search(el):
    tmp = [[el[0] + 1, el[1]], [el[0], el[1] + 1], [el[0] - 1, el[1]], [el[0], el[1] - 1]]
    for tmp_el in tmp:
      if tmp_el in arr and not tmp_el in result:
        result.append(tmp_el)
        search(tmp_el)        

  for _ in range(K):
    X, Y = map(int, sys.stdin.readline().split())
    arr.append([X, Y])
  
  arr.sort()

  for el in arr:
    if not el in result:
      cnt += 1
      result.append(el)
      search(el)



  print(cnt)


# DFS로 풂.