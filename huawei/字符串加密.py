while True:
    try:
        lineCode , line = raw_input() , raw_input()
        code = []
        res = ''
        for i in lineCode:
            if i not in code:
                code.append(i)
        for i in range(97,123):
            if chr(i) not in code:
                code.append(chr(i))
        for i in line:
            res += code[ord(i)-97]
        print res
    except:
        break