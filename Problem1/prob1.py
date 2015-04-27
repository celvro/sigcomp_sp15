a,b,c,d = (int(n) for n in raw_input().split())

while any([a,b,c,d]):
    count = 0
    while not a == b == c == d:
        temp = a
        a = abs(a-b)
        b = abs(b-c)
        c = abs(c-d)
        d = abs(d-temp)
        count+=1
    print count
    a,b,c,d = (int(n) for n in raw_input().split())