# https://www.acmicpc.net/problem/1927



# 힙이란?
# 이진트리. 각 노드의 index는 위에서 아래, 왼쪽에서 오른쪽 순이다. root 노드의 index는 1. 다음 2열의 왼쪽노드는 2, 오른쪽노드는 3.
# 각 노드의 parent 노드의 index는 i // 2 이다.
# list로 구현할 수도 있지만 heapq를 많이 사용한다.
# https://www.fun-coding.org/Chapter11-heap.html 삽입 및 삭제 시 처리 참고
# https://www.daleseo.com/python-heapq/


import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for i in range(N):
  number = int(sys.stdin.readline())
  if number == 0:
    if len(heap) > 0:
      v = heapq.heappop(heap)
      print(v)
    else:
      print(0)
  else:
    heapq.heappush(heap, number)
