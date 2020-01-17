while True:
    try:
        n = int(raw_input())
        ans = -1
        if n <= 2:
            ans = -1
        elif n % 2 == 1:
            ans = 2
        elif n % 4 == 0:
            ans = 3
        else:
            ans = 4
        print ans
    except:
        break
