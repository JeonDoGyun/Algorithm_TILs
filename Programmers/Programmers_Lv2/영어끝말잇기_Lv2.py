def solution(n, words):
    answer = []
    used_words = []
    number, turn = 0, 0
    used_words.append(words[0])
    last_word = words[0][-1]

    for i in range(1, len(words)):
        if words[i] not in used_words and words[i][0] == last_word:
            used_words.append(words[i])
            last_word = words[i][-1]
        else:
            number = (i % n)+1
            turn = (i//n)+1
            break
    answer = [number, turn]

    return answer
