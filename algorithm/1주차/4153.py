import sys


while True:
  x, y, z = map(int, sys.stdin.readline().split(" "))  

  arr = [x**2, y**2, z**2]

  if arr == [0, 0, 0]:
    break

  if arr[0] + arr[1] == arr[2] or arr[0] + arr[2] == arr[1] or arr[1] + arr[2] == arr[0]:
    print("right")
  else:
    print("wrong")
