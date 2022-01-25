import sys

cnt = int(sys.stdin.readline())
arr = []

for _ in range(cnt):
  arr.append(sys.stdin.readline().strip())

arr = list(set(arr))

arr.sort()
arr.sort(key=len)    

for char in arr:
  print(char)


# https://www.acmicpc.net/problem/1181
# sort() 안쓰고 아래와 같이 구현했다가 시간초과 떠서 sort() 써서 위와 같이 구현


cnt = int(input())
original_arr = []
result_arr = []

for _ in range(cnt):
  original_arr.append(input())

original_arr = list(set(original_arr))
result_arr.append(original_arr[0])

def compare_ascii(el1, el2):
  result = False
  for i in range(len(el1)):
    if ord(el1[i]) < ord(el2[i]):
      result = True
      break
  return result

for original_el in original_arr:
  copy_arr = result_arr[:]
  for i, result_el in enumerate(copy_arr):
    if len(original_el) < len(result_el):
      result_arr.insert(i, original_el)
      break
    elif len(original_el) == len(result_el):
      if compare_ascii(original_el, result_el):
        result_arr.insert(i, original_el)
        break
    

for char in result_arr:
  print(char)