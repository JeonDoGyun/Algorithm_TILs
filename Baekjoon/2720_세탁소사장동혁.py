t = int(input())
coins = [25, 10, 5, 1]

for _ in range(t):
    array = []
    charge = int(input())
    for coin in coins:
        array.append(charge//coin)
        charge %= coin

    for i in array:
        print(i, end=' ')
