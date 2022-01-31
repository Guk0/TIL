import sys

n, m = map(int, sys.stdin.readline().split(" "))
arr = [i for i in range(1, n+1)]
result = []

index = 0
while len(arr) > 0:
  index += m-1
  if index >= len(arr):
    if len(arr) <= m:
      index = index % len(arr)
    else:
      index -= len(arr)

  result.append(arr[index])
  del arr[index]


print("<", end="")
for index, num in enumerate(result):
  if index == len(result) - 1:
    print(num, end="")
  else:
    print(num, end=", ")
print(">")

# import sys

# n, m = map(int, sys.stdin.readline().split(" "))
# arr = [i for i in range(1, n+1)]
# result = []


# cnt = 0
# index = 0
# while len(result) != len(arr):
#   if not arr[index] in result:
#     if cnt == m-1:
#       result.append(arr[index])
#       cnt = 0
#     else:
#       cnt += 1
#       index += 1
#       if index == len(arr):
#         index = 0

#   else:    
#     index += 1
#     if index == len(arr):
#       index = 0

# print("<", end="")
# for index, num in enumerate(result):
#   if index == len(result) - 1:
#     print(num, end="")
#   else:
#     print(num, end=", ")
# print(">")