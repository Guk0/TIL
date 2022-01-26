import sys
import math

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
cnt = 0

for i in arr:
	if i == 1:
		continue
	sqrt = math.floor(math.sqrt(i))
	result = True	
	for j in range(2, sqrt + 1):
		if i % j == 0:
			result = False
	if result:
		cnt += 1

print(cnt)