# https://www.acmicpc.net/problem/1074
# Z
# 재귀

import sys

N, r, c = map(int, sys.stdin.readline().split(" "))


def check(n, y, x):
  if n == 0:
    return 0

  share = 2**(n-1)
  start = int(4**n / 4)

  if y < share:
    if x < share:
      start = 0
    else:
      x -= share
      start *= 1
  else:
    if x < share:
      y -= share
      start *= 2
    else:
      y -= share
      x -= share
      start *= 3

  return start + check(n-1, y, x)
  
print(check(N, r, c))



# 22 4/20 풀이
# def check(n, r, c, start, end):
#   global answer
#   if start == end:
#     answer = start
#     return
#   mid = 2**(n-1)
#   gap = 2**((n-1)*2)

#   if r < mid and c < mid:
#     check(n-1, r, c, start, start+gap-1)
#   elif r < mid and c >= mid:
#     check(n-1, r, c-mid, start+gap, start+gap*2-1)
#   elif r >= mid and c < mid:
#     check(n-1, r-mid, c, start+gap*2, start+gap*3-1)
#   else:
#     check(n-1, r-mid, c-mid, start+gap*3, start+gap*4-1)

# N, r, c = map(int, input().split())
# answer = 0
# check(N, r, c, 0, (2**N)**2)
# print(answer)