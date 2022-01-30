a, b, v = map(int, input().split(" "))

v = v - b
result = v // (a-b)

if v % (a-b) > 0:
  print(result + 1)
else:
  print(result)

