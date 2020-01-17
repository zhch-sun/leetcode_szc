# 其实就是回溯法. 

def printf(temp):
    for i in temp:
        print ('(%d,%d)' % (i[0],i[1]))
def maze(xy,array,row,col):
    if xy[0] == row-1 and xy[1] == col-1:
        printf(temp)
    if xy[1]-1 >= 0:
        if array[xy[0]][xy[1]-1] != 1 and array[xy[0]][xy[1]-1] != 'X':
            array[xy[0]][xy[1]-1] = 'X'
            temp.append([xy[0],xy[1]-1])
            maze([xy[0],xy[1]-1],array,row,col)
    if xy[1]+1 < col:
        if array[xy[0]][xy[1]+1] != 1 and array[xy[0]][xy[1]+1] != 'X':
            array[xy[0]][xy[1]+1] = 'X'
            temp.append([xy[0],xy[1]+1])
            maze([xy[0],xy[1]+1],array,row,col)
    if xy[0]-1 >= 0:
        if array[xy[0]-1][xy[1]] != 1 and array[xy[0]-1][xy[1]] != 'X':
            array[xy[0]-1][xy[1]] = 'X'
            temp.append([xy[0]-1,xy[1]])
            maze([xy[0]-1,xy[1]],array,row,col)
    if xy[0]+1 < row:
        if array[xy[0]+1][xy[1]] != 1 and array[xy[0]+1][xy[1]] != 'X':
            array[xy[0]+1][xy[1]] = 'X'
            temp.append([xy[0]+1,xy[1]])
            maze([xy[0]+1,xy[1]],array,row,col)
     
    if len(temp) != 0:
        temp.pop()
    return
   
       
while True:
    try:
        rowCol = raw_input().split()
        row = int(rowCol[0])
        col = int(rowCol[1])
        array = []
        global temp
        temp = [[0,0]]
         
        for i in range(row):
            temp1 = map(int,raw_input().split())
            array.append(temp1)
        array[0][0] = 'X'
        maze([0,0],array,row,col)
    except:
        break
            