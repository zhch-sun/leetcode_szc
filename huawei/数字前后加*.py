#-*- coding:utf8 -*-
import sys
while True:
    try:
        reload(sys)
        a , b , c = u'零壹贰叁肆伍陆柒捌玖' , u'拾佰仟' , u'角分'
        num = raw_input()
 
        def func2(s):
            res = u''
            count = len(s)
            for i in s:
                if count == 1:
                    res += a[int(i)]
                elif count == 2 and int(i) == 1:
                    res += u'拾'
                else:
                    res += a[int(i)]
                    res += b[count-2]
                count -= 1                  
            return res
 
        def func(num):
            res = u'人民币'
            if len(num) > 8:
                res += func2(num[0:-8])
                res += u'亿'
            if len(num) > 4:
                res += func2(num[-8:-4])
                res += u'万'
            if len(num) > 0:
                res += func2(num[-4:])
                res += u'元'
            return res
 
        if '.' in num:
            num = num.split('.')
            if int(num[0]) != 0:
                chineseNum = func(num[0])
            else:
                chineseNum = u'人民币'
            for i in range(len(num[1])):
                if int(num[1][i]) != 0:
                    chineseNum += a[int(num[1][i])]
                    chineseNum += c[i]
        else:
            chineseNum = func(num)
            chineseNum += u'整'
 
        print chineseNum
    except:
        break