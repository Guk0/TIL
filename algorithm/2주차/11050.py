from math import factorial
import sys

n, m = map(int, sys.stdin.readline().split(" "))

def factorial(x):
  if x > 1:
    result = x * factorial(x-1)
  else:
    result = 1
  return result


num = factorial(n) / (factorial(n-m) * factorial(m))

print(int(num))