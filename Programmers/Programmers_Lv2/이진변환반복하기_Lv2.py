s = "01110"
count = 0
zero = 0

while s != '1':
    new_s = ''
    for number in s:
        if number == '0':
            zero += 1
        elif number == '1':
            new_s += number
    count += 1
    s = str(bin(len(new_s)))[2:]

print([count, zero])
