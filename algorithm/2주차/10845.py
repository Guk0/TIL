import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
  order = sys.stdin.readline().strip("\n")
  try:
    operator, number = order.split(" ")
  except:
    operator = order
  if operator == 'push':
    arr.append(int(number))
  elif operator == 'pop':
    if len(arr) > 0:
      print(arr.pop(0))
    else:
      print(-1)
  elif operator == 'size':
    print(len(arr))
  elif operator == 'empty':
    print(1 if len(arr) == 0 else 0)
  elif operator == 'front':
    if len(arr) > 0:
      print(arr[0])
    else:
      print(-1)
  elif operator == 'back':
    if len(arr) > 0:
      print(arr[-1])
    else:
      print(-1)
