while True:
    try:
        s1=raw_input()
        s2=raw_input()
        count=0
        idx=[0,1]
        n,m=len(s1),len(s2)
        if n<m:
            for i in range(n):
                for j in range(i,n):
                    if s1[i:j+1] in s2:
                        if j+1-i>count:
                            count=j+1-i
                            idx[0]=i
                            idx[1]=j+1
            print s1[idx[0]:idx[1]]
        else:
            for i in range(m):
                for j in range(i,m):
                    if s2[i:j+1] in s1:
                        if j+1-i>count:
                            count=j+1-i
                            idx[0]=i
                            idx[1]=j+1
            print s2[idx[0]:idx[1]]                
    except:
        break
