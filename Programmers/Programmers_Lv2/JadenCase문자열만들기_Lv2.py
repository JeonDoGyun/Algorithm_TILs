def solution(s):
    result = ''
    a = 0
    for i in range(len(s)):
        if i == 0:
            result += s[i].upper()
            continue

        if s[i] == ' ':
            a += 1
            result += s[i]
        else:
            if a != 0:
                result += s[i].upper()
                a = 0
            else:
                result += s[i].lower()
    return result
