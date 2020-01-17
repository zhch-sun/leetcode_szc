try:
    while True:
        num=int(raw_input())
        L=[[0 for i in range(0)] for j in range(num)]
        insert=1
        for i in range(num):
            for j in range(i+1):
                L[i-j].append(str(insert))
                insert=insert+1
        for i in range(num):
            print ' '.join(L[i])
except:
    pass