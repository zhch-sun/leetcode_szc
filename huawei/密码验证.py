def checklen(s):
    if len(s) >8:
        return True
    else:
        return False
  
def check2(s):
    flag_up,flag_low,flag_digit,flag_other = 0,0,0,0
    for i in s:
        if i.isupper():
            flag_up = 1
        elif i.islower():
            flag_low = 1
        elif i.isdigit():
            flag_digit = 1
        else:
            flag_other = 1
     
    if (flag_up+flag_low+flag_digit+flag_other)>=3:
        return True
    else:
        return False
  
def check3(s):
    for i in range(len(s)-3):
        if s.count(s[i:i+3]) >1:
            return False    
    return True
 
while True:
    try:
        s = raw_input()
        if checklen(s) and check2(s) and check3(s):
            print "OK"
        else:
            print "NG"
 
    except Exception,e:
        break
    