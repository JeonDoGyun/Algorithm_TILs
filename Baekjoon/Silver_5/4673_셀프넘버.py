def self_search():
    num = set(range(1, 10001))
    unself_num = set()

    for i in range(1, 10001):
        for j in str(i):
            i += int(j)

        unself_num.add(i)

    self_num = sorted(list(num - unself_num))

    for i in self_num:
        print(i)


self_search()
