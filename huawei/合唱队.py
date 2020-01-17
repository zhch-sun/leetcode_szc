def LIS(n):
    B = [n[0]]
    dp = [1]
    for i in range(1,len(n)):
        left = 0
        right = len(B)-1
        pos = 0
        while left <= right:
            mid = (left+right)//2
            if B[mid] == n[i]:
                pos = mid
                break
            if B[mid] > n[i]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            pos = left
        dp.append(pos + 1)
        try:
            B[pos] = n[i]
        except:
            B.append(n[i])
    return dp
try:
    while True:
        N = int(raw_input())
        students = map(int,raw_input().split())
        left_right = LIS(students)
        right_left = LIS(students[::-1])
        right_left=right_left[::-1]
        max_r = max([left_right[i] + right_left[i]-1 for i in range(N)])
        print N - max_r
except:
    pass