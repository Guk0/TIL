# https://www.acmicpc.net/problem/1620
# 나는야 포켓몬 마스터 이다솜
# 해시

# dic.values에 index로 접근하는 방식으로 하면 시간초과 발생
# > values = list(dic.values())
# > print(values.index(char) + 1)

# dic에 key를 int와 char 둘 다 적용

import sys

N, M = map(int, sys.stdin.readline().split(" "))
dic = {}

for i in range(1, N+1):
  name = sys.stdin.readline().strip("\n")
  dic[i] = name
  dic[name] = i

for _ in range(M):
  char = sys.stdin.readline().strip("\n")
  if char.isdigit():
    print(dic[int(char)])
  else:
    print(dic[char])