def solution(genres, plays):
    answer = []
    temp = []
    genre_dict = {}
    
    temp = [[genres[i], plays[i], i] for i in range(len(genres))]
    temp = sorted(temp, key=lambda x: (x[0], -x[1], x[2]))
    
    for i in temp:
        if i[0] not in genre_dict:
          genre_dict[i[0]] = i[1]
        else:
          genre_dict[i[0]] += i[1]
    genre_dict = sorted(genre_dict.items(), key=lambda x: -x[1])
    
    for i in genre_dict:
      count = 0
      for j in temp:
        if i[0] == j[0]:
          count += 1
          if count > 2:
            break
          else:
            answer.append(j[2])
            
    return answer