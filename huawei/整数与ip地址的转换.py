
while True:
    try:
        strs = raw_input().split('.')
        nums = map(int, strs)
        res = (nums[0] << 24) + (nums[1] << 16) + (nums[2] << 8) + nums[3]
        print res 

        num = int(raw_input())
        print('.'.join([str(num // (256 ** i) % 256) for i in range(3, -1, -1)]))
    except:
        break