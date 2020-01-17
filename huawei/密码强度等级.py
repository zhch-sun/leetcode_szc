while True:
    try:
        pw = raw_input()
        score = 0
        line = [0]*4#num, upper, lower, other
        for i in pw:
            if i.isdigit():
                line[0] += 1
            elif i.isupper():
                line[1] += 1
            elif i.islower():
                line[2] += 1
            else:
                line[3] += 1
        if len(pw) <= 4:
            score += 5
        elif len(pw) <= 7:
            score += 10
        else:
            score += 25
        if line[1] > 0:
            score += 10
        if line[2] > 0:
            score += 10
        if line[0] == 1:
            score += 10
        elif line[0] > 1:
            score += 20
        if line[3] == 1:
            score += 10
        elif line[3] > 1:
            score += 25
        if line[0] and line[1] and line[2] and line[3]:
            score += 5
        elif line[0] and line[3] and (line[1] or line[2]):
            score += 3
        elif line[0] and (line[1] or line[2]):
            score += 2
        if score >=90:
            print 'VERY_SECURE'
        elif score >=80:
            print 'SECURE'
        elif score >= 70:
            print 'VERY_STRONG'
        elif score >= 60:
            print 'STRONG'
        elif score >= 50:
            print 'AVERAGE'
        elif  score>=25:
            print 'WEAK'
        else:
            print 'VERY_WEAK'
    except:
        break
