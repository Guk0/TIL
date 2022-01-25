import sys

amount, target_cnt = map(int, sys.stdin.readline().split(" "))
line_arr = []

for _ in range(amount):
	line_arr.append(int(sys.stdin.readline().strip()))


min_l = 1
max_l = max(line_arr)


while min_l <= max_l:
	mid = (max_l + min_l) // 2
	cnt = 0
	for el in line_arr:
		cnt += el // mid
	
	if cnt >= target_cnt:
		min_l = mid + 1
	else:
		max_l = mid - 1

print(max_l)


# binary search를 사용하지 않고 풀다가 시간초과 뜸. 0부터 +1을 해서 찾는 것 보다 
# max number가 정해져 있다면 binary search를 사용하여 푸는게 시간 복잡도가 덜 함.