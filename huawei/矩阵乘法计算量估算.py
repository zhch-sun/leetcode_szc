while True:
    try:
        n=int(raw_input())
        shape=[]
        for _ in range(n):
            shape.append(map(int,raw_input().split()))
        exp=raw_input()
        stack=[]
        cnt=0
        for item in exp:
            if item=="(":
                pass
            elif item==")":
                try:
                    b=stack.pop()
                    a=stack.pop()
                    cnt+=a[0]*a[1]*b[1]
                    stack.append([a[0],b[1]])
                except:
                    break
            else:
                stack.append(shape[ord(item)-65])
        print cnt
    except:
        break