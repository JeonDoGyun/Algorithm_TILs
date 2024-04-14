import sys

n = int(input())
words = []

for _ in range(n):
  word = sys.stdin.readline().strip()
  length = len(word)
  words.append((word, length))

words = list(set(words))
words.sort(key=lambda x: x[0])
words.sort(key=lambda x: x[1])

for i in words:
  print(i[0])