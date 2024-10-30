n = int(input())
count = 0
a = n//10
b = n % 10

while True:
    c = (a+b) % 10
    m = b*10+c
    a = m//10
    b = m % 10
    count += 1
    if n == m:
        break

print(count)
