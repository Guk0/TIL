# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상
# 스택

import sys

target_dict = {"(": ")", "[": "]"}

while True:
  arr = []
  result = True
  line = sys.stdin.readline().strip("\n")
  if line == '.':
    break

  for char in line:
    if char in ["(", ")", "[", "]"]:
      if char in list(target_dict.keys()):
        arr.append(char)
      elif len(arr) > 0 and target_dict[arr[-1]] == char:
        arr.pop()
      else:
        result = False
        break

  if len(arr) > 0:
    result = False

  print("yes" if result else "no")
  
