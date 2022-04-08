# https://www.acmicpc.net/problem/10814
# 나이순 정렬
# 해시

import sys
n = int(sys.stdin.readline())

age = {}

for _ in range(n):
  x, y = sys.stdin.readline().strip("\n").split(" ")
  x = int(x)

  try:  
    age[x].append(y)
  except: 
    age[x] = [y]

for i in sorted(list(age.keys())):
  for j in age[i]:
    print(i, end=" ")
    print(j)
