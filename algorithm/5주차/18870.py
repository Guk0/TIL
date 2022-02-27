# https://www.acmicpc.net/problem/18870
# 좌표압축

# .index method는 O(n)의 시간 복잡도. for 문을 돌며 index를 찾는 것은 결국 O(n^2)의 시간복잡도를 갖게 된다. 따라서 dictionary로 풀어야 함.

from sys import stdin

N = int(stdin.readline())

arr = list(map(int, stdin.readline().split()))

sorted_arr = list(sorted(set(arr)))
dic = {sorted_arr[i]: i for i in range(len(sorted_arr))}

for i in arr:
  print(dic[i], end=' ')


# from sys import stdin

# N = int(stdin.readline())

# arr = list(map(int, stdin.readline().split()))

# sorted_arr = list(sorted(set(arr)))

# for i in arr:
#   print(sorted_arr.index(i), end=' ')
