x, y, w, h = map(int, input().split(" "))

print(min(y, h-y, x, w-x))


# https://www.acmicpc.net/problem/1085
# (x, 0) (x, h) (0, y) (w, y)
#   y     h-y    x      w-x