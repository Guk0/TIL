import sys

length = int(sys.stdin.readline())

target_arr = [int(sys.stdin.readline().strip()) for _ in range(length)]
stack = []
result = []
operator_arr = []

for i in range(0, length):
	stack.append(i + 1)
	operator_arr.append("+")
	while stack[len(stack) - 1] == target_arr[len(result)]:
		result.append(stack.pop())
		operator_arr.append("-")
		if len(stack) == 0:
			break


if result == target_arr:
	for el in operator_arr:
		print(el)
else:
	print("NO")


# 스택과 list가 있고 스택을 이용하여 list가 주어진 수열과 같게 만드는 문제.
# stack 의 마지막 el과 target_arr를 비교. 
# stack의 마지막 숫자가 target_arr의 result 다음 el과 같으면 while문을 돌려서 stack에서 빼고 result에 append한다.