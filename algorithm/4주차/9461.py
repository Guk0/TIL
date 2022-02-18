# https://www.acmicpc.net/problem/9461
# 파도반 수열


# [0, 1, 1, 1, 2]

# 5 0 0
# 6 1 1
# 7 1 2
# 8 1 3
# 9 2 4

# 2 0
# 2 1
# 3 1
# 4 1
# 5 2
# 7 2


from sys import stdin

N = int(stdin.readline())

for _ in range(N):
  M = int(stdin.readline().strip())
  initial_arr = [0, 1, 1, 1, 2, 2]
  if M <= 5:
    print(initial_arr[M])
  else:
    for i in range(6, M+1):
      initial_arr.append(initial_arr[i-1] + initial_arr[i-5])
    print(initial_arr[-1])