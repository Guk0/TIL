import sys
n = int(sys.stdin.readline())

for _ in range(n):
  H, W, cnt = map(int, sys.stdin.readline().split(" "))

  share = cnt // H
  remain = cnt % H
  if remain != 0:
    share += 1
  else:
    remain = H

  print(str(remain * 100 + share))