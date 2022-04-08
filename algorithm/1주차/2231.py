# https://www.acmicpc.net/problem/2231
# 분해합

import sys

n = int(sys.stdin.readline())
number = 1

while True:
	if number > n:
		print(0)
		break

	result = number

	for i in str(number):
		result += int(i)
    
	if result == n:
		print(number)
		break
	else:
		number += 1