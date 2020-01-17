def main(i,n,a,result,s):#n=len(a) a=[] result=0 s=abs(sum1-sum2)
    if i==n:
        return abs(result)==s
    else:
        return (main(i+1,n,a,result+a[i],s) or main(i+1,n,a,result-a[i],s))

while True:
    try:
        n=input()
        nums=raw_input().strip()
        nums=map(int,nums.split(' '))
        if sum(nums)%2 != 0:
            print 'false'
        else:
            num5=[]
            num3=[]
            a=[]
            for x in nums:
                if x%5==0:
                    num5.append(x)
                elif x%3==0:
                    num3.append(x)
                else:
                    a.append(x)
            sum1=sum(num5)
            sum2=sum(num3)            
            count=len(a)
            s=abs(sum1-sum2)
            if main(0,count,a,0,s):
                print 'true'
            else:
                print 'false'
    except:
        break