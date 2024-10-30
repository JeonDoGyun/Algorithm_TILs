number, b = map(int, input().split())
array = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = ''

while number:
    s += array[number % b]
    number //= b

print(s[::-1])
