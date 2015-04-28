rows, cols = (int(i) for i in raw_input().split())

while any([rows,cols]):
    M = []
    for i in range(rows):
        line = raw_input().strip()
        x = []
        for c in line:
            if c=='.': 
                x.append(1)
            else:
                x.append(0)
        M.append(x)
        
    for i in range(1, rows):
        for j in range(1, cols):
            if M[i][j]==1:
                M[i][j] = min(M[i-1][j], M[i][j-1], M[i-1][j-1]) + 1
            else:
                M[i][j] = 0

    m = 0 # max square size
    for i in M:
        m = max(m, max(i))
    if m==0:
        print 'NO'
    else:
        print m
    
    rows, cols = (int(i) for i in raw_input().split())
    