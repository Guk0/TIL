# https://www.acmicpc.net/problem/2869
# 달팽이는 올라가고 싶다

a, b, v = map(int, input().split(" "))

v = v - b
result = v // (a-b)

if v % (a-b) > 0:
  print(result + 1)
else:
  print(result)

