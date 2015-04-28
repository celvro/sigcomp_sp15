# N = num of customers, pA = pizzas at A, pB = pizzas at B
N, pA, pB = (int(i) for i in raw_input().split())

while any([N,pA,pB]):
    # list of lists, num pizzas and distance for A and B 
    data = []

    for i in range(N):
        n,dA,dB = (int(i) for i in raw_input().split())
        data.append([n,dA,dB])

    # Sorting by most cost effective pizzas to deliver first
    data.sort(key=lambda x: abs(x[1]-x[2]))

    total_dist = 0
    for i in data:
        while i[0]:
            if (i[1]<i[2] and pA) or not pB:
                total_dist+=i[1]
                pA-=1
            else:
                total_dist+=i[2]
                pB-=1
            i[0]-=1
    print total_dist
    N, pA, pB = (int(i) for i in raw_input().split())