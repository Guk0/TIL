# https://www.acmicpc.net/problem/16236
# 아기 상어


# 아기상어는 자신보다 작은 물고기만 먹을 수 있음.
# 먹을 수 있는 물고기가 없다면 엄마에게 도움. 끝
# 여러마리를 먹을 수 있는경우 가장 가까운 물고기를 먹음. 위에 있는 물고기, 
# 상어의 크기는 2. 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1씩 증가.
# 자기보다 큰 물고기는 지나갈 수 없음. 같을떄는 가능.


from sys import stdin
from collections import deque

N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
queue = deque()
time = 0

def bfs():
  queue.



# https://yunanp.tistory.com/12


