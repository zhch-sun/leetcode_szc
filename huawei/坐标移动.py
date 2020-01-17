try:
    while True:
        dirs = {'A': (-1, 0), 'D': (1, 0),
                'W': (0, 1), 'S': (0, -1)}
        inputs = raw_input().split(';')
        out = []
        pos = [0, 0]
        for tmp in inputs:
            tmp = tmp.strip()
            if not tmp:
                continue
            if tmp[0] not in dirs.keys():
                continue
            if len(tmp[1:]) > 2 or len(tmp[1:]) == 0:
                continue
            if not tmp[1:].isdigit():
                continue
            arrow = dirs[tmp[0]]
            length = int(tmp[1:])
            pos[0] += arrow[0] * length
            pos[1] += arrow[1] * length
        print str(pos[0]) + ',' + str(pos[1])

except:
    pass