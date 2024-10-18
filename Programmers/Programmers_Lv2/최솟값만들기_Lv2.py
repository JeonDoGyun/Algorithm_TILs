A = [1, 2]
B = [3, 4]

print(sum([a*b for a, b in zip(sorted(A), sorted(B, reverse=True))]))
