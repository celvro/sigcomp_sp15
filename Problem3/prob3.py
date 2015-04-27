def max_subarray(l):
    test_max = l[0]
    curr_max = l[0]
    for x in l[1:]:
        test_max = max(x, test_max+x)
        curr_max = max(curr_max, test_max)
    return curr_max
    
n = int(raw_input())

while n:
    l = list()
    for i in range(n):
        l.append(int(raw_input()))
    
    print(max_subarray(l))
    n = int(raw_input())
