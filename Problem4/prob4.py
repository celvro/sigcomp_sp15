def vampire(a,b):
    return sorted(str(a*b)) == sorted(str(a)+str(b))
    
MAX = 1000300

x = set()
for i in range(1, MAX):
    for j in range(i, MAX//i):
        if vampire(i,j):
            x.add(i*j)
x = sorted(x)

n = int(raw_input())

while n:
    for i in x:
        if i>=n:
            print i
            n = int(raw_input())
            break
    print "Not found"
    break