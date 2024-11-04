n = int(input())
count = 0
word = 666

while True:
  if '666' in str(word):
    count += 1
  
  if count == n:
    break
  
  word += 1

print(word)