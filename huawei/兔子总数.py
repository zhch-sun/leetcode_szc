while True:
    try:
        month=int(raw_input())
        if month<3:
            print 1
        else:
            a=1
            b=1
            for i in range(3,month+1):
                a,b=b,a+b
            print b
    except:
        break
         