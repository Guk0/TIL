# https://www.acmicpc.net/problem/10816
# 숫자카드
# 해시, 이분탐색(해시로 풀긴했는데 이분탐색이 깔끔한듯)


import sys

n = int(sys.stdin.readline())
card_arr = map(int, sys.stdin.readline().split(" "))

m = int(sys.stdin.readline())
target_arr = map(int, sys.stdin.readline().split(" "))

cnt_dict = {}

for i in card_arr:
  try:
    cnt_dict[i] += 1
  except:
    cnt_dict[i] = 1

for i in target_arr:
  try:
    print(cnt_dict[i], end=" ")
  except:
    print(0, end=" ")
  