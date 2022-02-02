# https://www.acmicpc.net/problem/1463
# 1로 만들기
# DP

# 시작점과 끝점(n)이 주어져 있으니 1부터 n까지 모든 count를 계산. dictionary에 i를 key로, count를 value로 저장.
# 1~10까지 최소 count를 계산해놓고 11부터 최소 count를 계산한다.
# 각각 i-1, i/3, i/2를 키로 갖는 value 중 제일 작은 값을 선택. 해당 값에 +1을 하여 i의 value로 한다.

import sys


n = int(sys.stdin.readline())
dic = {1: 0, 2: 1, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3, 8: 3, 9: 2, 10: 3}

for i in range(11, n+1):
  min_count = dic[i-1]
  if i % 3 == 0 and min_count > dic[i/3]:
    min_count = dic[i/3]
  if i % 2 == 0 and min_count > dic[i/2]:
    min_count = dic[i/2]
  
  dic[i] = min_count + 1
    



print(dic[n])