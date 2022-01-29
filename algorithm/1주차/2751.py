import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
	arr.append(int(sys.stdin.readline()))

arr.sort()

for i in arr:
	print(i)

# pypy3을 써서 푼다.
# recursion error 때문에 아래와 같이 재귀로 풀기 어렵다.
# 결국엔 그냥 내장함수 써야할듯.

# import sys
# sys.setrecursionlimit(1000000)

# n = int(sys.stdin.readline())
# arr = []

# for _ in range(n):
# 	arr.append(int(sys.stdin.readline()))

# def partition(low, high):
# 	pivot = arr[(low + high)//2]
# 	while low <= high:
# 		while arr[low] < pivot:
# 			low += 1
# 		while arr[high] > pivot:
# 			high -= 1
		
# 		if low <= high:
# 			arr[low], arr[high] = arr[high], arr[low]
# 			low += 1
# 			high -= 1
# 	return low

# def quick_sort(low, high):
# 	if high <= low:
# 		return	
# 	mid = partition(low, high)
# 	quick_sort(low, mid - 1)
# 	quick_sort(mid, high)


# quick_sort(0, len(arr) - 1)

# for i in arr:
# 	print(i)


