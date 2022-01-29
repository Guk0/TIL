import sys

n, m = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

maximum = 0

for i in range(n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      result = arr[i] + arr[j] + arr[k]
      if maximum < result and result <= m:
        maximum = result
      
print(maximum)

# permutation 쓰면?

# import sys

# n, m = map(int, sys.stdin.readline().split(" "))
# arr = list(map(int, sys.stdin.readline().split(" ")))

# i = 0
# j = 1
# k = 2
# maximum = 0

# while i < n - 2:
#   while j < n - 1:
#     while k < n:
#       result = arr[i] + arr[j] + arr[k]
#       if maximum < result and result <= m:
#         maximum = result
#       k += 1
#     j += 1
#     k = j + 1
#   i += 1
#   j = i + 1
#   k = j + 1

# print(maximum)