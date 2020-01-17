while True:
    try:
        string1=raw_input()
        string2=raw_input()
        l1=len(string1)
        l2=len(string2)
        dp=[[False]*(l2+1) for _ in range(l1+1)]
        dp[0][0]=True
        if string1[0]=='*':
            dp[1][0]=True
        for i in range(1,l1+1):
            for j  in range(1,l2+1):
                if string1[i-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i-1][j]
                elif string1[i-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=dp[i-1][j-1] and string1[i-1]==string2[j-1]
        if  dp[l1][l2]==True:
            print 'true'
        else:
            print 'false'
    except:
        break