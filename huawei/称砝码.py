while True:
    try:
        n = input()
        m = map(int, raw_input().split())
        x = map(int, raw_input().split())
        diff = {0}
         
        for i in range(n):
            temp = diff.copy()
            for j in range(x[i]):
                for k in temp:
                    d = k + m[i] * (j + 1)
                    if d not in temp:
                        diff.add(d)
        print len(diff)
    except:
        break