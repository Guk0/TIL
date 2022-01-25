import sys
import math

while True:
  number = sys.stdin.readline().strip()
  if number == "0":
    break
  else:
    arr = list(map(int, number))
    length = len(arr)
    index = math.floor(length / 2)
    result = True
    for i in range(index):
      if arr[i] != arr[length -1 -i]:
        print("no")
        result = False
        break
    if result:
      print("yes")



#파이썬의 리스트 슬라이싱(number[::-1]) 을 활용하면 훨씬 쉽게 풀 수 있음.

import sys
import math

while True:
  number = sys.stdin.readline().strip()
  if number == "0":
    break
  else:
    if number == number[::-1]:
      print("yes")
    else:
      print("no")
