# https://www.acmicpc.net/problem/2805
# 나무자르기
# 이분탐색(binary search)

import sys

n, m = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

result = 0
min_num, max_num = 0, max(arr)

while min_num <= max_num:
  mid = (min_num + max_num) // 2
  sumation = 0
  sumation = sum([i-mid if mid < i else 0 for i in arr])

  if sumation < m:
    max_num = mid - 1
  else:
    result = mid
    min_num = mid + 1    

print(result)




# 그냥 풀면 시간초과. binary search로 풀어야함.
# for i in arr:
#   if mid < i:
#     sumation = i - mid
# 위 구문보다 sum[] 구문이 훨씬 빠르다고 함.


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
