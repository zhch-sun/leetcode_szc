import sys
 
def f(m,n):
    if m < 0 or n < 0:
        return 0
    elif m ==1 or n == 1:
        return 1
    else:
        return f(m,n-1)+f(m-n,n)
while True:
    line1 = sys.stdin.readline().strip()
    if line1 == '':
        break
    line2 = line1.split(' ')
    m,n = map(int,line2)
    print f(m,n)
