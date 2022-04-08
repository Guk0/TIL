# https://www.acmicpc.net/problem/2292
# 벌집

# cnt는 1씩 늘어나면서  result 에 6*cnt 씩 더함. result가 n보다 크면 print하고 break

import sys

n = int(sys.stdin.readline())

cnt = 1
result = 1

while True:
	if n == 1:
		print(1)
		break
	result += 6*cnt
	cnt += 1
	if n <= result:
		print(cnt)
		break
	
