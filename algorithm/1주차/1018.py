# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기
# 부르트포스(모든 경우의 수를 계산해야함)


n, m = map(int, input().split(" "))
original = []
count = []

for _ in range(n):
  original.append(input())
    
for a in range(n-7):
  for b in range(m-7):
    index1 = 0
    index2 = 0
    
    for i in range(8):
      for j in range(8):
        if (i+j) % 2 == 0:
          if original[a+i][b+j] == "W":
            index1 += 1
          else:
            index2 += 1
        else:
          if original[a+i][b+j] == "B":
            index1 += 1
          else:
            index2 += 1
    count.append(min(index1, index2))

print(min(count))


# 첫번째 색깔을 바꾸는 경우가 더 횟수가 작은 경우를 고려 안하고 그냥 고정인 상태로 최소값을 구하는 로직을 짬.
# 위와 같이 변경.