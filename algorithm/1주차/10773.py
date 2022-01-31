import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
  m = int(sys.stdin.readline())
  if m == 0:
    if len(arr) > 0:
      arr.pop()
  else:
    arr.append(m)

print(sum(arr))  