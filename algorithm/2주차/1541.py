# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호

# 음수가 하나 나오는 순간 모든 +는 음수처리해도 됨. 그게 최소값
# 55-50+40-50-40-50+10 일때 55-(50+40)-50-40-(50+10)가 최소값
# 55-50+40+50+40+50+10 일때 55-(50+40+50+40+50+10)가 최소값
# 개선
# - 기준으로 split하고 index 0 번 제외 전부 합해서 index 0 - 나머지 로 구해도 될 듯.

arr = input().split("+")
arr2 = []

for el in arr:
  tmp = el.split("-")
  for index, el2 in enumerate(tmp):
    if index > 0:
      arr2.append(-int(el2))
    else:
      arr2.append(int(el2))


flag = False
total = 0

for i in arr2:
  if i > 0:
    if flag:
      total -= i
    else:
      total += i
  else:
    total += i
    if not flag:
      flag = True


print(total)


# >>> arr = "55-50+40-50-40-50+10".split("+")
# ['55-50', '40-50-40-50', '10']
# [55, -50, 40, -50, -40, -50, 10]
