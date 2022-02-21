# https://www.acmicpc.net/problem/11723
# 집합


from sys import stdin

N = int(stdin.readline())
set_list = set([])

for _ in range(N):
  operations = stdin.readline().strip().split(" ")
  if len(operations) == 1:
    if operations[0] == "all":
      set_list = set([i for i in range(1, 21)])
    else:
      set_list = set()

  else:
    operation, number = operations
    number = int(number)

    if operation == "add":
      set_list.add(number)
    elif operation == "remove":
      set_list.discard(number)
    elif operation == "check":
      print(1 if number in set_list else 0)
    elif operation == "toggle":
      if number in set_list:
        set_list.discard(number)
      else:
        set_list.add(number)



# set(집합)의 연산
# remove(원소) : 원소가 없는 경우 keyError
# discard(원소) : 원소가 없어도 keyError 발생 x
# {1, 2, 3, 4} & {1} -> 1이 있을경우 {1} 없으면 set() 반환
# {1, 2, 3, 4} | {5} -> {1, 2, 3, 4, 5} 반환