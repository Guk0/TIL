# https://www.acmicpc.net/problem/11399
# ATM
# 그리디

from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split(" ")))
cnt = 0
total = 0

arr.sort()

for i in arr:  
  cnt += i
  total += cnt

print(total)