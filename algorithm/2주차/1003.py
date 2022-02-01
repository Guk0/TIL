import sys

n = int(sys.stdin.readline())
dic = {0: [1, 0], 1: [0, 1]}

for _ in range(n):
  m = int(sys.stdin.readline())
  
  for i in range(2, m+1):
    dic[i] = [0,0]
    dic[i][0] = dic[i-1][0] + dic[i-2][0]
    dic[i][1] = dic[i-1][1] + dic[i-2][1]

  print(dic[m][0], dic[m][1])