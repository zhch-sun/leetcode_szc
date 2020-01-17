while True:
    try:
        m=int(raw_input().split()[0])
        p,q=map(int,raw_input().split())
        print p,q
        for i in range(m-1):
            x,y=map(int,raw_input().split())
            if x==p:
                pass
            elif x==p+1 or x<p:
                print x,y
                p,q=x,y
            else:
                for j in range(1,x-p):
                    t=(y-q)/(x-p)
                    if t>=0:
                        t=int(t)
                    else:
                        if float(y-q)/float(x-p)==float(t):
                            t=int(t)
                        else:
                            t=int(t)+1
                    print p+j,q+t*j
                print x,y
                p,q=x,y
    except:
        break