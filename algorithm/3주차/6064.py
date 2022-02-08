# https://www.acmicpc.net/problem/6064
# 카잉 달력 

# 마지막 해는 M, N 의 최소 공배수. while의 탈출조건.
# x를 초기화하지 않고 쭉 늘어뜨린 수와 y값은 N으로 나눴을때 나머지가 같다.
#  -> cnt를 M씩 늘려 N으로 나눈 값이 y를 N으로 나눈 값과 비교.

from sys import stdin

T = int(stdin.readline())

for i in range(T):
  M, N, x, y = map(int, stdin.readline().split(" "))
  cnt = x
  result = False

  while cnt == x or (cnt-x)%N != 0 :
    if cnt % N == y % N:
      result = True
      break

    cnt += M
    
  print(cnt if result else -1)

# 10, 12일때 경우의 수

# 1 1
# 2 2
# 3 3
# 4 4
# 5 5
# 6 6
# 7 7
# 8 8
# 9 9
# 10 10
# 11 11
# 12 12
# 13 1
# 14 2
# 15 3
# 16 4
# 17 5
# 18 6
# 19 7
# 20 8
# 21 9
# 22 10
# 23 11
# 24 12
# 25 1
# 26 2
# 27 3
# 28 4
# 29 5
# 30 6
# 31 7
# 32 8
# 33 9
# 34 10
# 35 11
# 36 12
# 37 1
# 38 2
# 39 3
# 40 4
# 41 5
# 42 6
# 43 7
# 44 8
# 45 9
# 46 10
# 47 11
# 48 12
# 49 1
# 50 2
# 51 3
# 52 4
# 53 5
# 54 6
# 55 7
# 56 8
# 57 9
# 58 10
# 59 11
# 60 12


# 시간초과

# from sys import stdin

# T = int(stdin.readline())

# for i in range(T):
#   M, N, x, y = map(int, stdin.readline().split(" "))
#   m, n = [1, 1]
#   cnt = 1
#   result = False

#   while True:    
#     if [m, n] == [x, y]:
#       result = True
#       break
      
#     if [m, n] == [M, N]:
#       break

#     cnt += 1

#     m = m + 1 if m < M else 1
#     n = n + 1 if n < N else 1

#   print(cnt if result else -1)


