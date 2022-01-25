import sys
import math

N, M = map(int, sys.stdin.readline().split(" "))

for i in range(N, M+1):
  sqrt = math.floor(math.sqrt(i))
  result = True
  if i == 1:
    continue
  for j in range(2, sqrt+1):
    if i % j == 0:
      result = False
      break
  if result:
    print(i)


# 소수 구하는 문제
# 제곱근 까지만 돌리면 N(logn)
# 6000ms 나왔는데 더 줄일 수 있는 방법이 있을까