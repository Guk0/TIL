import sys

n = int(sys.stdin.readline())
result = {}

for _ in range(n):
  x, y = map(int, sys.stdin.readline().split(" "))

  try:
    result[y].append(x)
  except:
    result[y] = [x]


for i in sorted(list(result.keys())):
  for j in sorted(result[i]):
    print(j, i)
