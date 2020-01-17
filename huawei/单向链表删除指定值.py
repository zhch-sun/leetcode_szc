while True:
    try:
        s=raw_input().split(' ')
        Node=int(s[0])
        a=[]
        a.append(int(s[1]))
        k=2
        for i in range(Node-1):
            m,n=int(s[k]),int(s[k+1])
            a.insert(a.index(n)+1,m)
            k=k+2
        a.remove(int(s[-1]))
        for i in a[:-1]:
            print i,
        print a[-1],
        print ''
    except:
        break