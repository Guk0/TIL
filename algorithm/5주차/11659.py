# https://www.acmicpc.net/problem/11659
# 구간 합 구하기4

# 0 ~ 구간까지의 합을 el로 하는 새로운 list를 만듦.
# x가 1일때는 index y-1의 값
# x가 1 이상일 때는 index y-1의 값 - x-2의 값.

from sys import stdin


N, M = map(int, stdin.readline().split(" "))

arr = list(map(int, stdin.readline().split(" ")))
sum_arr = []
cnt = 0

for i in arr:
  cnt += i
  sum_arr.append(cnt)


for _ in range(M):
  x, y = map(int, stdin.readline().split(" "))
  
  if x == 1:    
    print(sum_arr[y-1])
  else:
    print(sum_arr[y-1] - sum_arr[x-2])
