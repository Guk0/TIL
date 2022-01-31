import sys

n = int(sys.stdin.readline())
line = sys.stdin.readline().strip("\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = 0

for index, char in enumerate(line):
  num = alphabet.index(char) + 1
  result += num * (31 ** index)
  
print(result % 1234567891)