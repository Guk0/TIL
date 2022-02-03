# https://www.acmicpc.net/problem/1780
# 종이의 개수
# 재귀

# 인덱스 잘 나눠서 재귀 호출하는 것이 중요.
# check 함수 내에 2중 for문이 돌고 2중 for문 최대 호출 횟수가 약 4,000,000(3^7 * 3^7)이므로 break 설정을 꼭 해줘야 함.
# check를 9번 하드코딩으로 호출하는 것 말고 for 문 돌려서 호출하는 방법으로 바꿔야 좀 깔끔할 듯.

import sys

N = int(sys.stdin.readline())
arr = []
dic = {0: 0, 1: 0, -1: 0}

for _ in range(N):
  arr.append(list(map(int, sys.stdin.readline().split(" "))))

def check(x, y, n):  
  target = arr[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if target != arr[i][j]:
        target = -2
        break
    if target == -2:
      break
  
  if target == 0:
    dic[0] += 1
  elif target == 1:
    dic[1] += 1
  elif target == -1:
    dic[-1] += 1
  else:
    if n >= 3:
      n2 = int(n/3)
      check(x, y, n2)
      check(x, y + n2, n2)
      check(x, y + n2 * 2, n2)
      check(x + n2, y, n2)
      check(x + n2, y + n2, n2)
      check(x + n2, y + n2 * 2, n2)
      check(x + n2 * 2, y, n2)
      check(x + n2 * 2, y + n2, n2)
      check(x + n2 * 2, y + n2 * 2, n2)


check(0, 0, N)

print(dic[-1])
print(dic[0])
print(dic[1])