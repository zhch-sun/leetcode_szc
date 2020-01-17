while True:
    try:
        line = raw_input().split()
        line = line[0]+line[1]
        lineA , lineB, lineRes, lineTrans= '' , '', '', ''
        for i in range(len(line)):
            if i%2 == 0:
                lineA += line[i]#oushu
            else :
                lineB += line[i]#jishu
        lineA, lineB = sorted(lineA), sorted(lineB)
        for i in range(len(lineB)):
            lineRes += lineA[i]
            lineRes += lineB[i]
        if len(lineA) > len(lineB):
            lineRes += lineA[i+1]
 
        for i in lineRes:
            if i in '0123456789abcdefABCDEF':
                temp = bin(int('0x'+i,16))[2:]
                temp = (4-len(temp))*'0' + temp
                temp = (hex(int(temp[::-1],2))[2:]).upper()
            else:
                temp = i
            lineTrans += temp
        print lineTrans
    except:
        break