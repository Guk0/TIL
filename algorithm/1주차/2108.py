import sys

n = int(sys.stdin.readline())
arr = []


for _ in range(n):
	arr.append(int(sys.stdin.readline().strip()))

sorted_arr = sorted(arr)

def arr_average(array):
	value = 0
	for i in array:
		value += i
	return round(value / n)

def arr_mid(array):
	return array[len(array) // 2]

def frequent(array):
	num_dict = {}	
	for i in array:
		try:
			num_dict[i] += 1
		except:
			num_dict[i] = 1
	frequent_dict = {}
	for k, v in num_dict.items():
		try:
			frequent_dict[v].append(k)
		except:
			frequent_dict[v] = [k]
	key = sorted(list(frequent_dict.keys()))[-1]	
	return sorted(frequent_dict[key])[1] if len(frequent_dict[key]) > 1 else frequent_dict[key][0]

def arr_range(array):
	return array[-1] - array[0] if len(array) >= 2 else 0


print(arr_average(arr))
print(arr_mid(sorted_arr))
print(frequent(arr))
print(arr_range(sorted_arr))


# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# dict를 두개 만들어 num_dict는  key에 el, value에 count를 담고 frequent_dict는 key에 count, value에 el list를 담는다.
# 즉 아래와 같은 모양
# {4000: 2, 4001: 2, 4003: 1, 4004: 2}
# {1: [4001], 2: [4000, 4003, 4004}

#frequent_dict의 key를 sort하여 마지막 index의 key를 가져와 해당 키의 list를 sort하여 인덱스 1의 값을 return한다.