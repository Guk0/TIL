# https://www.acmicpc.net/problem/17626
# Four Squares

from sys import stdin


N = int(stdin.readline())
result = []

def check(num, target):
  if target == 0:
    return

  while True:
    if (num + 1) ** 2 > target:      
      check(1, target - num ** 2)
      if len(result) > 3 and num > 1:
        check(1, target - (num-1) ** 2)

      result.append(num)
      break
    else:
      num += 1

check(1, N)
print(result)


