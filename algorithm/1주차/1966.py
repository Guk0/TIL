# https://www.acmicpc.net/problem/1966
# 프린터 큐
# 큐

import sys

N = int(sys.stdin.readline())

for _ in range(N):
  amount, index = map(int, sys.stdin.readline().split(" "))
  priority = list(map(int, sys.stdin.readline().split(" ")))
  
  arr = [i for i in range(amount)]
  target = arr[index]
  cnt = 0
  
  while True:
    result = True
    for i in priority:
      if priority[0] < i:
        result = False
    if result:
      poped = arr.pop(0)
      pri_popped = priority.pop(0)
      cnt += 1
      if poped == target:
        break
    else:
      arr.append(arr.pop(0))
      priority.append(priority.pop(0))
  print(cnt)

# Queue
