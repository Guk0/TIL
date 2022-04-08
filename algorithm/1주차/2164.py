# https://www.acmicpc.net/problem/2164
# 카드 2
# 큐, deque

import sys

n = int(sys.stdin.readline())

arr = [i for i in range(1, n + 1)]


while len(arr) != 1:
	pop1 = arr.pop(0)
	pop2 = arr.pop(0)
	arr.append(pop2)

print(arr[0])


# 위와 같은 방법으로 시도했는데 n ≤ 500000이라 최악의 경우 10초 이상 걸림
# pop말고 del, array slicing도 성능은 마찬가지.

# 큐에서 성능 문제가 날 것 같으면 deque를 사용하여 풀자.


import sys
from collections import deque


n = int(sys.stdin.readline())
queue = deque()

for i in range(1, n + 1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())