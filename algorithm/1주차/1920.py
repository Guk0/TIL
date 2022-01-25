import sys

N = int(sys.stdin.readline())
target_arr = list(map(int, sys.stdin.readline().split(" ")))
target_arr.sort()
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))

for i in arr:
  min_index = 0
  max_index = len(target_arr) - 1
  while min_index <= max_index:  
    mid_index = (min_index + max_index) // 2    
    if target_arr[mid_index] > i:
      max_index = mid_index - 1
    elif target_arr[mid_index] < i:
      min_index = mid_index + 1
    else:
      print("1")
      break
  print("0")

# 이진탐색