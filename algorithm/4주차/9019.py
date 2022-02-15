# https://www.acmicpc.net/problem/9019
# DSLR

# pypy3로 통과

from sys import stdin
from collections import deque


def operation_D(number):
  return 2*number if number < 5000 else 2*number - 10000

def operation_S(number):
  return number-1 if number > 0 else 9999

def operation_L(number):  
  return (number % 1000)*10 + (number // 1000)

def operation_R(number):  
  return (number % 10) * 1000 + (number // 10)

def bfs(x, y):
  queue = deque()  
  queue.append([x, ""])
  visited = [False] * 10001
  while queue:
    number, operators = queue.popleft()

    if number == y:
      print(operators)
      break

    D = operation_D(number)
    if not visited[D]:
      queue.append([D, operators + "D"])
      visited[D] = True
    
    S = operation_S(number)
    if not visited[S]:
      queue.append([S, operators + "S"])
      visited[S] = True

    L = operation_L(number)
    if not visited[L]:
      queue.append([L, operators + "L"])
      visited[L] = True
    
    R = operation_R(number)
    if not visited[R]:
      queue.append([R, operators + "R"])
      visited[R] = True

N = int(stdin.readline())

for _ in range(N):
  x, y = map(int, stdin.readline().split(" "))
  bfs(x, y)