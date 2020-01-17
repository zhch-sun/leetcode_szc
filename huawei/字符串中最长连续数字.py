import sys
while True:
    try:
        line = raw_input()
        maxCount = 0
        digitLine = ''
        for i in range(len(line)):
            if line[i].isdigit():
                digitLine += line[i]
            else:
                digitLine += '#'
        digitArray = digitLine.split('#')
        for i in digitArray:
            maxCount = max(maxCount , len(i))
        for i in digitArray:
            if len(i) == maxCount:
                sys.stdout.write(i),
        print ','+str(maxCount)
    except:
        break
