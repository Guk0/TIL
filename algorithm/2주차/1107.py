# https://www.acmicpc.net/problem/1107
# 리모컨
# brute force

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
removed = []
if M > 0:
  removed = list(map(int, sys.stdin.readline().split(" ")))

cnt = abs(N - 100)

for i in range(1000001):
  result = True
  for j in str(i):
    if int(j) in removed:
      result = False
      break
  if result:
    cnt = min(cnt, len(str(i)) + abs(N - i))


print(cnt)


# 마지막에 100에서부터 직접 + 혹은 -를 눌러서 간 것도 계산해서 둘 중 작은 숫자로 해야함.
# removed가 0~9까지 모든 수에 해당하면서 N이 한자리일 때 number = 무조건 0으로 나옴. 따라서 number 초기값을 -1로 하고 -1일때는 무조건 abs(N-100)으로 해야함.