
while True:
    try:
        password = raw_input()
        encodepw = []
        for i in password:
            if '0'<= i <= '9':
                encodepw.append(i)
            elif 'A'<= i <= 'Z':
                i = chr((ord(i.lower())+1-97)%26+97)
                encodepw.append(i)
            elif i in 'abc':
                encodepw.append('2')
            elif i in 'def':
                encodepw.append('3')
            elif i in 'ghi':
                encodepw.append('4')
            elif i in 'jkl':
                encodepw.append('5')
            elif i in 'mno':
                encodepw.append('6')
            elif i in 'pqrs':
                encodepw.append('7')
            elif i in 'tuv':
                encodepw.append('8')
            elif i in 'wxyz':
                encodepw.append('9')
            else:
                break
        print ''.join(encodepw)
 
    except:
        break
    