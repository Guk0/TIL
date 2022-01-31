import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque()

for _ in range(n):
  order = sys.stdin.readline().strip("\n")
  try:
    operator, number = order.split(" ")
  except:
    operator = order
    
  if operator == 'push_front':
    deq.appendleft(int(number))
  elif operator == 'push_back':
    deq.append(int(number))
  elif operator == 'pop_front':
    if len(deq) > 0:
      print(deq.popleft())
    else:
      print(-1)
  elif operator == 'pop_back':
    if len(deq) > 0:
      print(deq.pop())
    else:
      print(-1)
  elif operator == 'size':
    print(len(deq))
  elif operator == 'empty':
    print(1 if len(deq) == 0 else 0)
  elif operator == 'front':
    if len(deq) > 0:
      print(deq[0])
    else:
      print(-1)
  elif operator == 'back':
    if len(deq) > 0:
      print(deq[-1])
    else:
      print(-1)