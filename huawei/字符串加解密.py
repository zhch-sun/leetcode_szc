while True:
    try:
        s1 = raw_input()
        s2 = raw_input()
         
        add_password = ''
         
        for each in s1:
            if each.isdigit():
                n = int(each)
                if n != 9:
                    add_password += str(n + 1)
                else:
                    add_password += '0'
            else:
                if each.islower():
                    if each != 'z':
                        add_password += chr(ord(each) - 31)
                    else:
                        add_password += 'A'
                else:
                    if each != 'Z':
                        add_password += chr(ord(each) + 33)
                    else:
                        add_password += 'a'
                         
                         
                         
        decode_password = ''
         
        for each in s2:
            if each.isdigit():
                n = int(each)
                if n != 0:
                    decode_password += str(n - 1)
                else:
                    decode_password += str('9')
            else:
                if each.islower():
                    if each != 'a':
                        decode_password += chr(ord(each) - 33)
                    else:
                        decode_password += 'Z'
                else:
                    if each != 'A':
                        decode_password += chr(ord(each) + 31)
                    else:
                        decode_password += 'z'
                         
        print add_password
        print decode_password
         
    except:
        break