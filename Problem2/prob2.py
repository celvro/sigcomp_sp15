def palindrome(n):
    return str(n) == str(n)[::-1]
    
num = str(raw_input()).strip()
l = len(num)

while num!='0':
    temp = num
    p = '{:0'+str(l)+'d}'
    num = int(num)
    while not palindrome(p.format(num)):
        num += 1
    print int(num)-int(temp)
    num = str(raw_input()).strip()
    l = len(num)