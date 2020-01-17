while True:
    try:
        year,month,day=map(int,raw_input().split())
        if (year%4==0 and year%100!=0) or year%400==0:
            days_per_month=[31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            days_per_month=[31,28,31,30,31,30,31,31,30,31,30,31]
        outDay=0
        for i in range(month-1):
            try:
                outDay+=days_per_month[i]
            except:
                print -1
                break
        if (day>=1 and day<=days_per_month[month-1]):
            outDay+=day
            print outDay
        else:
            print -1
            break
    except:
        break