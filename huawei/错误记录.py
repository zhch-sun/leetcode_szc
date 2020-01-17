d = {}
name = []
while True:
    try:
        inputs = raw_input().split(' ')
        fname = inputs[0].split('\\')[-1][-16:]
        line = inputs[1]
        key = fname + ' ' + line
        if key not in d:
            name.append(key)
            d[key] = 1
        else:
            d[key] += 1
    except:
        break
for item in name[-8:]:
    num = d[item]
    print item + ' ' + str(num)