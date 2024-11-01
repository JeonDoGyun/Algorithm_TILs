while True:
    number = int(input())
    array = []
    sum = 0

    if number == -1:
        break

    for i in range(1, number):
        if number % i == 0:
            array.append(i)
            sum += i

    if number == sum:
        print(f'{number} = ', end='')
        for i in array:
            if i == array[-1]:
                print(i)
            else:
                print(i, end=' + ')
    else:
        print(f'{number} is NOT perfect.')
