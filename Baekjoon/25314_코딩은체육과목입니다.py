n = int(input())

if n % 4 == 0:
    count = n//4
else:
    count = n//4+1


word = 'long ' * count + 'int'
print(word)
