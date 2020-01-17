while True:
    try:
        s = raw_input()
        s1 = s[::-1]
        f = 0
        for i in range(1,len(s)+1)[::-1]:
            if f == 1:
                break
            for j in range(len(s)+1-i):
                ts = s[j:j+i]
                #print i,j,ts
                if s1.count(ts) > 0 and ts == ts[::-1]:
                    print i
                    f = 1
                    break
    except:
        break