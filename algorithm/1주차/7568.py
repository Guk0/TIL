# https://www.acmicpc.net/problem/7568
# 덩치

import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
  arr.append(list(map(int, sys.stdin.readline().split(" "))))

for x in arr:
  rank = 1
  for y in arr:
    if x[0] < y[0] and x[1] < y[1]:
      rank += 1
  print(rank, end = " ")


# import sys

# n = int(sys.stdin.readline())
# arr = []
# rank_arr = []

# for _ in range(n):
#   el = list(map(int, sys.stdin.readline().split(" ")))
#   rank = max(rank_arr) if len(rank_arr) > 0 else 1

#   if len(arr) > 0:
#     tmp_arr = arr[:]
#     for i, num_arr in enumerate(tmp_arr):
#       if el[0] == num_arr[0] and el[1] == num_arr[1]:
#         rank = rank_arr[i]
#       elif el[0] > num_arr[0] and el[1] > num_arr[1]:
#         rank = rank_arr[i] if rank_arr[i] < rank else rank
#         rank_arr[i] += 1
#       elif el[0] <= num_arr[0] and el[1] <= num_arr[1]:
#         rank = rank_arr[i] + 1
#       else:
#         rank = rank_arr[i] if rank_arr[i] < rank else rank

#   arr.append(el)
#   rank_arr.append(rank) 

# rank_arr2 = sorted(set(rank_arr))
# for i, rank in enumerate(rank_arr2):
#   count = rank_arr.count(rank)
#   if count > 1 and i+1 < len(rank_arr2):
#     rank_arr2[i+1] = rank + count
#
#
# for i, rank in enumerate(rank_arr):
#   rank_arr[i] = rank_arr2[rank-1]
#
#
# print(rank_arr)
