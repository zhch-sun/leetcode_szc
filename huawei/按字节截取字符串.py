while True:
    try:
        a, b = raw_input().split()
        print a[:int(b)]
    except:
        break