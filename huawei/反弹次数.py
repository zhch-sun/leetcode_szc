import sys
 
while True:
    try:
        string = sys.stdin.readline()
        number = int(string)
        print '%g' % (2.875 * number)
        print '%g' % (0.03125 * number)
    except:
        break