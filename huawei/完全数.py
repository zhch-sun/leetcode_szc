while True:
    try:
        N = int(raw_input())
        total = 0
        for i in range(1,N + 1):
            s=0
            for k in range(1, i // 2 + 1):
                if i%k==0:
                    s=s+k
            if i==s:
                total += 1
        print(total)
    except:
        break