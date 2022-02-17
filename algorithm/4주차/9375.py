# https://www.acmicpc.net/problem/9375
# 패션왕 신해빈


# 안 입는 경우의 수도 포함하여 조합을 구해야함. 마지막에 모두 안 입는 경우의 수는 빼줌.
# hat headgear
# sunglasses eyewear
# turban headgear
# 의 경우 2, 1가지 이지만 안 입는 경우가 있으니 3C1 * 2C1 - 1
#
# mask face
# sunglasses face
# makeup face
# 의 경우 4C1 - 1



from sys import stdin

N = int(stdin.readline())

for _ in range(N):
  M = int(stdin.readline())
  dic = {}

  for _ in range(M):
    clothes, kind = stdin.readline().strip().split(" ")
    try:
      dic[kind].append(clothes)
    except:
      dic[kind] = [clothes]

  count = 1
  arr = list(dic.values())  

  for el in arr:
    count *= (len(el)+1)
  print(count-1)




# from sys import stdin

# N = int(stdin.readline())

# def combination(index):
#   global count, arr

#   if index >= len(arr):
#     return

#   for el in arr[index]:
#     count += 1    
#     for i in range(index, len(arr)):
#       combination(i+1)


# for _ in range(N):
#   M = int(stdin.readline())
#   dic = {}

#   for _ in range(M):
#     clothes, kind = stdin.readline().strip().split(" ")
#     try:
#       dic[kind].append(clothes)
#     except:
#       dic[kind] = [clothes]

#   count = 0
#   arr = list(dic.values())  

#   for i in range(len(arr)):
#     combination(i)
#   print(count)