# https://www.acmicpc.net/problem/9012
# 괄호
# 스택

import sys

n = int(sys.stdin.readline())



for _ in range(n):
  arr = []
  line = sys.stdin.readline().strip()
  result = True
  for i in line:
    if i == "(":
      arr.append(i)
    else:
      if len(arr) > 0 and arr[-1] == "(":
        arr.pop()
      else:
        result = False
        break

  print("YES" if result == True and len(arr) == 0 else "NO")
