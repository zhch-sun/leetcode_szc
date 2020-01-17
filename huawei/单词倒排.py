while True:
    try:
        b = []
        a = raw_input()
        for i in a:
            if not i.isalpha():
                a = a.replace(i,' ')
        for i in a.split():
            b.append(i)
        print " ".join(b[::-1])
    except:
        break