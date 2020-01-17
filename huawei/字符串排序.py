while True:
    try:
        s=raw_input()
        temp=list(s)     
        str1=filter(lambda x:x.isalpha(),list(s))
        str1.sort(key=str.upper)
        j=0
        for i in range(len(temp)):
            if temp[i].isalpha():
                temp[i]=str1[j]
                j+=1
        print ''.join(temp)
    except:
        break
