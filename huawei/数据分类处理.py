import sys
   
f = sys.stdin
   
def my_cmp(a, b):
    return int(a) - int(b)
   
while True:
    I = f.readline()
    if not I:
        break
    R = f.readline()
    I = I.split()[1:]
    R = sorted(list(set(R.split()[1:])), my_cmp)
    ans = []
    for r in R:
        r_ans = []
        for ii, i in enumerate(I):
            if r in i:
                r_ans.append(ii)
                r_ans.append(i)
        if r_ans:
            ans.append(r)
            ans.append(len(r_ans) / 2)
            ans += r_ans
    print len(ans),
    for a in ans:
        print a,
    print