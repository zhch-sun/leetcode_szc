class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        cur = str(self.val)
        return cur + ', ' + self.next.__repr__() if self.next else cur
        
def solution(total_num=50):
    dummy = Node(0)
    last = dummy
    for i in range(1, total_num + 1):
        node = Node(i)
        last.next = node
        last = node
    last.next = dummy.next
    
    cnt = 1
    pre = dummy
    cur = dummy.next
    while cur.next is not cur:
        if cnt % 7 == 0 or '7' in list(str(cnt)):
            pre.next = cur.next
        else:
            pre = cur
        cnt += 1
        cur = cur.next
    return cur.val

print(solution())