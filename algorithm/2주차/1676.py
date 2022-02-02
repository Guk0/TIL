# https://www.acmicpc.net/problem/1676
# 팩토리얼 0의 개수

# num을 list로 만들어 -1로 찍는 건 시간이 너무 오래걸림. 그냥 str로 변환해서 인덱스 찍는게 훨씬 빠름.
# 그래도 시간초과
# 0일때 예외처리
# while N != 1:  --> while N > 0:


N = int(input())
num = 1

while N > 0:
  num *= N
  N -= 1

number = str(num)
index = -1
cnt = 0

while int(number[index]) == 0:
  cnt += 1
  index -= 1

print(cnt)