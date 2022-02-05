# https://www.acmicpc.net/problem/2579
# 계단오르기
# DP

# DP
# 핵심 : max(result[i-2] + arr[i], result[i-3] + arr[i-1] + arr[i])


import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
result = [0] * 301



result[0] = arr[0]
if N >= 2:
  result[1] = max(arr[0] + arr[1], arr[1])

  if N >= 3:
    result[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, N):
      result[i] = max(result[i-2] + arr[i], result[i-3] + arr[i-1] + arr[i])


print(result[N-1])


# 재귀
# 재귀로 풀어도 되지만 시간초과. 규칙성이 보인다면 무조건 DP로 푸는 것이 시간복잡도를 줄이는 방법.

# import sys

# N = int(sys.stdin.readline())
# arr = [int(sys.stdin.readline()) for _ in range(N)]
# result = []

# def check(x, score, cnt):
#   if x >= N:
#     return

#   score += arr[x]
#   if x == N-1:
#     result.append(score)
#     return
#   print(x)
#   if cnt == 1:
#     check(x+1, score, 2)
#     check(x+2, score, 1)
#   else:
#     check(x+2, score, 1)

# print(max(result))

