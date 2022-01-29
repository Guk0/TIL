import sys

n, m = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

cnt = 0
min_num, max_num = min(arr), max(arr)

while True:
  mid = (min_num + max_num) // 2
  sumation = 0
  for j in arr:
    if i <= j:
      sumation += (j - i)
  if sumation == m:
    cnt = i

  if m > sumation:
    min_num = mid
  elif m < sumation:
    max_num = mid
    
print(cnt)


# 그냥 풀면 시간초과. binary search로 풀어야함.

# import sys

# n, m = map(int, sys.stdin.readline().split(" "))
# arr = list(map(int, sys.stdin.readline().split(" ")))

# cnt = 0

# for i in range(max(arr)):
#   sumation = 0
#   for j in arr:
#     if i <= j:
#       sumation += (j - i)
#   if sumation == m:
#     cnt = i
    
# print(cnt)
