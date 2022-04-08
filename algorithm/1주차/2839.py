# https://www.acmicpc.net/problem/2839
# 설탕배달
# 그리디

import sys

n = int(sys.stdin.readline())

five = n // 5
three_share = 0
three_remain = 0
while five >= 0:
  three_share = (n - five*5) // 3
  three_remain = (n - five*5) % 3
  if three_remain > 0:
    five -= 1

  if three_remain == 0:
    break

if three_remain == 0 and three_share + five > 0:
  print(five + three_share)
else:
  print(-1)


# 위도 맞는 풀이지만 아래 풀이가 더 깔끔할듯.
# n = int(input())
# result = 0

# while n >= 0:
#     if n % 5 == 0:
#         result += n // 5
#         print(result)
#         break
#     n -= 3
#     result += 1
# else:
#     print(-1)