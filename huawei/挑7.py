while True:
    try:
        N = input()
        count_7 = 0
        for i in xrange(7, N+1):
            if '7' in str(i) or i % 7 == 0:
                count_7 = count_7 + 1
        print count_7
    except:
        break