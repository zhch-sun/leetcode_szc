
while True:
    try:
        line = int(raw_input())

        count = 0
        while line > 1:
            if line <= 3:
                count += 1
                break
            else:
                more = line/3
                count += more
                line -= more*2
        print count
    except:
        break    