import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
removed = []
if M > 0:
  removed = list(map(int, sys.stdin.readline().split(" ")))

cnt = 0
number = 0

for i in range(1000001):
  result = True
  for j in str(i):
    if int(j) in removed:
      result = False
      break
  if result and abs(N - i) < abs(N - number):
    number = i

if number == 0:
  
cnt = len(str(number)) + abs(N - number)

print(min(cnt, abs(N - 100)))

# 마지막에 100에서부터 직접 + 혹은 -를 눌러서 간 것도 계산해서 둘 중 작은 숫자로 해야함.