import sys
from unittest import case

n = int(sys.stdin.readline())

arr = []

def push(x):
  arr.append(x)

def pop():
  if len(arr) > 0:
    print(arr.pop())
  else:
    print(-1)

def size():
  print(len(arr))

def empty():
  print(1 if len(arr) == 0 else 0)

def top():
  if len(arr) > 0:
    print(arr[-1])
  else:
    print(-1)

for _ in range(n):
  order = sys.stdin.readline().strip("\n")
  try:
    operator, number = order.split(" ")
  except:
    operator = order
  if operator == 'push':
    push(int(number))
  elif operator == 'pop':
    pop()
  elif operator == 'size':
    size()
  elif operator == 'empty':
    empty()
  elif operator == 'top':
    top()
