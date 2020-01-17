def init(row, line):
    if 0<=row<=9 and 0<= line<=9:
        a = [[i for i in range(line)] for j in range(row)]
        print 0
        return a
    else:
        print -1
  
def exchange(a,source, dest):
    if 0<= source[0] < len(a) and 0<= source[1] < len(a[0]) and 0<= dest[0] < len(a) and 0<= dest[1] < len(a[0]):
        a[dest[0]][dest[1]],a[source[0]][source[1]] = a[source[0]][source[1]], a[dest[0]][dest[1]]
        return 0
    else:
        return -1
    
def insert_line(a,insert_l):
    if 0<=insert_l<len(a):
        a.insert(insert_l,[0 for i in range(len(a[0]))])
        # for i in a:
        #     print i
        return 0
    else:
        return -1
  
def insert_column(a, insert_col):
    if 0<=insert_col<len(a[0]):
        for i in range(len(a)):
            a[i].insert(insert_col,0)
        # for i in a:
        #     print i
        return 0
    else:
        return -1
  
def search(a,search_grid,row, line):
    if 0<= search_grid[0] < row and 0<= search_grid[1] < line:
        return 0
    else:
        return -1
while True:
    try:
        row, line = [int(x) for x in raw_input().split()]
  
  
        a=init(row,line)
  
        source = [int(x) for x in raw_input().split()]
  
        print exchange(a,source[0:2],source[2:])
  
        ins_line = int(raw_input())
        # print "isnert line:", ins_line
        print insert_line(a, ins_line)
  
        ins_col = int(raw_input())
        print insert_column(a, ins_col)
  
        search_grid = [int(x) for x in raw_input().split()]
        print search(a, search_grid,row,line)
    except:
        break