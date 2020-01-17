import sys
  
def checkTwoKeys(twoKeys,a,result):
    count = 0
    index = 0
    for y in twoKeys:
        if a[0]==y.split()[0][:len(a[0])] and a[1]==y.split()[1][:len(a[1])]:
            count += 1
            index = twoKeys.index(y)
    if count > 1 or count == 0:
        print("unkown command")
    elif count == 1:
        print(result[index])
              
oneKey = 'reset'
twoKeys = ['reset board','reboot backplane','backplane abort','board add','board delete']
result = ['board fault','impossible','install first','where to add','no board at all']
for i in sys.stdin:
    a = i.strip().split()
    l = len(a)
    if l <= 0 or l>=3:
        print("unkown command")
    elif l == 1:
        if a[0] == oneKey[:len(a[0])]:
            print("reset what")
        else:
            print("unkown command")
    elif l == 2:
        checkTwoKeys(twoKeys,a,result)