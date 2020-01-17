while True:
    try:
        a,b = map(int,raw_input().split('/'))
        result = []
        while a!=1:
            if b%(a-1) == 0:
                result.append(str(1)+'/'+str(b/(a-1)))
                a = 1
            else:
                p = b/a
                q = b%a
                result.append(str(1)+'/'+str(p+1))
                a = a - q
                b = b*(p+1)
                if b%a==0:
                    b = b/a
                    a = 1
        result.append(str(1)+'/'+str(b))
        print '+'.join(result)
    except:
        break