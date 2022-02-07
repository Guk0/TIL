# https://www.acmicpc.net/problem/5430
# AC

import sys

N = int(sys.stdin.readline())

for _ in range(N):
  operation = list(sys.stdin.readline().strip())
  M = int(sys.stdin.readline())
  arr = sys.stdin.readline().strip().replace("[", "").replace("]","").split(",")
  arr = [] if M == 0 else arr
  is_reverse = False
  is_error = False
  
  for char in operation:
    if char == "R":
      is_reverse = not is_reverse
    else:
      if len(arr) > 0:
        if is_reverse:
          arr.pop()
        else:
          arr.pop(0)
      else:
        is_error = True
        break

  if is_error:
    print("error")
  else:
    if is_reverse:
      print("[" + ",".join(reversed(arr)) + "]")
    else:
      print("[" + ",".join(arr) + "]")