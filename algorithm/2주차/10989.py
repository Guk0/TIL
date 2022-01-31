import sys

n = int(sys.stdin.readline())
arr = [0] * 10001


for _ in range(n):
  num = int(sys.stdin.readline())
  arr[num] += 1


for index, cnt in enumerate(arr):
  if cnt > 0:
    for _ in range(cnt):
      print(index)