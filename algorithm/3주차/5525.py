# https://www.acmicpc.net/problem/5525
# IOIOI

# 시간복잡도 O(N)이 되도록 짜야함.
# 핵심은 arr[index-1] == "I" and arr[index] == "O" and arr[index+1] == "I"

from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

arr = list(stdin.readline().strip())
index = 1
count = 0
result = 0

while index+1 < M:
  if arr[index-1] == "I" and arr[index] == "O" and arr[index+1] == "I":
    count += 1
    index += 1
  else:
    count = 0

  if count == N:
    result += 1
    count -= 1
  index += 1

print(result)



# 50점짜리

# from sys import stdin

# N = int(stdin.readline())
# M = int(stdin.readline())
# cnt = 0

# target = ["I"]
# for _ in range(N):
#   target.append("O")
#   target.append("I")

# arr = list(stdin.readline().strip())

# for index, el in enumerate(arr):
#   if el == "I" and index < M - (N*2) and arr[index:index+len(target)] == target:
#     cnt += 1

# print(cnt)


# 50점. 리스트 슬라이싱 안쓰고

# from sys import stdin

# N = int(stdin.readline())
# M = int(stdin.readline())
# cnt = 0


# target = "I"
# target += "OI" * N
# result = ""
# arr = list(stdin.readline().strip())

# for el in arr:
#   if target[len(result)] == el:
#     result += el
#   elif el == "I":
#     result = "I"
#   else:
#     result = ""
    
#   if result == target:
#     cnt += 1
#     result = result[2:]

# print(cnt)
