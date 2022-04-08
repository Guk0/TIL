
# https://www.acmicpc.net/problem/1436
# 영화감독 숌 


import sys

number = int(sys.stdin.readline())
result = 666
count = 1

while count != number:
  result += 1
  if '666' in str(result):
    count += 1
    

print(result)


# 계속 1을 더 '666'이 들어가 있으면 count를 1 늘리는 식으로 구현