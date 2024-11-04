sum = 0
count = 0
for _ in range(20):
    subject, score, grade = map(str, input().split())
    if grade == 'P':
        continue
    else:
        match grade:
            case 'A+':
                sum += float(score) * 4.5
            case 'A0':
                sum += float(score) * 4.0
            case 'B+':
                sum += float(score) * 3.5
            case 'B0':
                sum += float(score) * 3.0
            case 'C+':
                sum += float(score) * 2.5
            case 'C0':
                sum += float(score) * 2.0
            case 'D+':
                sum += float(score) * 1.5
            case 'D0':
                sum += float(score) * 1.0
            case 'F':
                sum += float(score) * 0.0
        count += float(score)
print(sum/count)
