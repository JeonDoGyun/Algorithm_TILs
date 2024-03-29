def search_han():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        a = i//100
        b = (i//10)%10
        c = i%10

        if i<100:
            count+=1
        elif (a-b) == (b-c):
            count+=1
    
    print(count)

search_han()