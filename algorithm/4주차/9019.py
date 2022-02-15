# https://www.acmicpc.net/problem/9019
# DSLR

from sys import stdin
from collections import deque


def operation_D(number):
  return 2*number if number < 5000 else 2*number - 10000

def operation_S(number):
  return number-1 if number > 0 else 9999

def operation_L(number):
  char_number = str(number)
  char_number = "0" * (4 - len(char_number)) + char_number
  arr = list(char_number)
  arr.append(arr.pop(0))

  return int("".join(arr))

def operation_R(number):
  char_number = str(number)
  char_number = "0" * (4 - len(char_number)) + char_number
  arr = list(char_number)
  arr.insert(0, arr.pop())

  return int("".join(arr))



def bfs(x, y):
  queue = deque()  
  queue.append([x, ""])
  visited = [x]
  while queue:
    number, operators = queue.popleft()

    if number == y:
      print(operators)
      break

    D = operation_D(number)
    if not D in visited:
      queue.append([D, operators + "D"])
      visited.append(D)
    
    S = operation_S(number)
    if not S in visited:
      queue.append([S, operators + "S"])
      visited.append(S)

    L = operation_L(number)
    if not L in visited:
      queue.append([L, operators + "L"])
    
    R = operation_R(number)
    if not R in visited:
      queue.append([R, operators + "L"])


N = int(stdin.readline())

for _ in range(N):
  x, y = map(int, stdin.readline().split(" "))
  bfs(x, y)