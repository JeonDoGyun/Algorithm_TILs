word = input().lower()  # mississipi
word_list = list(set(word))  # m, i, s, p
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)  # [4, 4, 1, 1]

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))].upper())
