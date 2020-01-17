A, B, C, D, E = 0, 0, 0, 0, 0
error=0
private=0

def check_ip(ip):
    if len(ip) != 4 or '' in ip:
        return False
    for item in ip:
        if item == '' or not (0 <= int(item) <= 255):
            return False
    return True

def check_mask(mask):
    # 255.255.255.255是错的. 必须至少有一个0
    s = ''  # 把它们连起来.. 找到第一个为0的位置. 看后面是否全0
    for i in mask:
        if not i.isdigit() or int(i) < 0 or int(i)> 255:
            return False
        str1 = bin(int(i))[2:]
        str2 = '0'*(8-len(str1))+str1
        s += str2
    zero = s[s.find('0'):]
    if int(zero)!=0:
        return False
    return True

while True:
    try:
        string = raw_input().strip()
        tmp = string.split("~")
        ip = tmp[0].split('.')
        ms = tmp[1].split('.')
        if check_mask(ms) and check_ip(ip):
            if 1 <= int(ip[0]) <= 126:
                A += 1
            elif 128 <= int(ip[0]) <= 191:
                B += 1
            elif 192 <= int(ip[0]) <= 223:
                C += 1
            elif 224 <= int(ip[0]) <= 239:
                D += 1
            elif 240 <= int(ip[0]) <= 255:
                E += 1
            if int(ip[0])==10 or (int(ip[0])==172 and 15<int(ip[1])<32) or (int(ip[0])==192 and int(ip[1])==168):
                private += 1
        else:
            error += 1
    except:
        break
print "%s %s %s %s %s %s %s" %(A,B,C,D,E,error,private)
