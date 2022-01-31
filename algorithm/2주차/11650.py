import sys

n = int(sys.stdin.readline())
result = {}

for _ in range(n):
  x, y = map(int, sys.stdin.readline().split(" "))

  try:
    result[x].append(y)
  except:
    result[x] = [y]


for i in sorted(list(result.keys())):
  for j in sorted(result[i]):
    print(i, j)


# 그냥 2중 리스트로 받아서 sorted 해도 되긴함.