import sys

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
	arr.append(int(sys.stdin.readline()))

def partition(low, high):
	pivot = arr[(low + high)//2]
	while low <= high:
		while arr[low] < pivot:
			low += 1
		while arr[high] > pivot:
			high -= 1
		
		if low <= high:
			arr[low], arr[high] = arr[high], arr[low]
			low += 1
			high -= 1
	return low

def quick_sort(low, high):
	if high <= low:
		return	
	mid = partition(low, high)
	quick_sort(low, mid - 1)
	quick_sort(mid, high)


quick_sort(0, len(arr) - 1)

print(arr)