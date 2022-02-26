# https://www.acmicpc.net/problem/17219
# 비밀번호 찾기


from sys import stdin

N, M = map(int, stdin.readline().split())
dic = {}



for _ in range(N):
  x, y = stdin.readline().strip().split()
  dic[x] = y

for _ in range(M):
  url = stdin.readline().strip()
  print(dic[url])
