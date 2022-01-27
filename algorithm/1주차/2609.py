import sys

n, m = map(int, sys.stdin.readline().split(" "))

def maximum(n, m):
	num1 = min(n, m)
	num2 = max(n, m)
	cnt = 1
	result = 1
	for i in range(1, num1 + 1):
		if num1 % cnt == 0:
			if num2 % cnt == 0:
				result = cnt
		cnt += 1
	return result


max_num = maximum(n, m)
min_num = n * m // max_num

print(max_num)
print(min_num)


# 최소 공배수는 두 수의 곱 / 최대 공약수 로 계산한다.