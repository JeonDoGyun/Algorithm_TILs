n = int(input())

count = 0
row = [0] * n

def attack(x):
  for i in range(x):
    if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
      return False
  return True

def queen(start):
  global count
  if start == n:
    count += 1
    return
  else:
    for i in range(n):
      row[start] = i
      if attack(start):
        queen(start+1)

queen(0)
print(count)