# https://www.acmicpc.net/problem/1085
# 직사각형에서 탈출

x, y, w, h = map(int, input().split(" "))

print(min(y, h-y, x, w-x))


# (x, 0) (x, h) (0, y) (w, y)
#   y     h-y    x      w-x