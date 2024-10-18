n = 15
k = n+1
while True:
    if str(bin(n)).count('1') == str(bin(k)).count('1'):
        answer = k
        break
    else:
        k += 1
print(answer)
