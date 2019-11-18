#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#

def list2Node(input):
    dummy = Node(None, None, None)
    cur = dummy
    tmp = []
    for item in input:
        cur.next = Node(item[0], None, None)
        cur = cur.next
        tmp.append(cur)  # Note 这个append的顺序很重要
    
    cur = dummy.next
    for item in input:
        cur.random = tmp[item[1] - 1]
        cur = cur.next
    return dummy.next

# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    def __repr__(self):
        next = ',' + self.next.__repr__() if self.next else ''
        random = str(self.random.val) if self.random else 'None'
        return str(self.val) + ' ' + random + ' ' + next

class Solution(object):
    # def copyRandomList(self, head):
    #     """
    #     :type head: Node
    #     :rtype: Node
    #     """           
    #     if not head:  # 没有dummy时checkhead
    #         return head
    #     tmp = {}
    #     cur = head
    #     while cur:
    #         tmp[cur] = Node(cur.val, None, None)
    #         cur = cur.next
    #     cur = head
    #     while cur:
    #         if cur.next:  # 需要判断..
    #             tmp[cur].next = tmp[cur.next]
    #         if cur.random:
    #             tmp[cur].random = tmp[cur.random]
    #         cur = cur.next  # 忘记了!!!
    #     return tmp[head]

    # def copyRandomList(self, head):
    #     # 不写这个, 太麻烦
    #     def getNew(old):
    #         if old in tmp:
    #             return tmp[old]
    #         else:
    #             new = Node(old.val, None, None)
    #             tmp[old] = new
    #             return new
        
    #     if not head:
    #         return None
    #     tmp = {}
    #     old = head
    #     new = getNew(old) # 这里也调函数
    #     while old is not None:
    #         new.random = getNew(old.random)
    #         new.next = getNew(old.next)
    #         old = old.next
    #         new = new.next
    #     return tmp[head]

    def copyRandomList(self, head):
        if not head:
            return head
        
        cur = head
        while cur:  # 建立node, 连next
            new = Node(cur.val, cur.next, None)
            cur.next = new
            cur = new.next
        
        cur = head  # copy random
        while cur:
            new = cur.next
            new.random = cur.random.next if cur.random else None  # Note 必须判断..
            cur = new.next
        
        cur = head
        cur1 = head1 = head.next
        while cur1.next:  # 拆开. 注意写法
            cur.next = cur.next.next
            cur1.next = cur1.next.next
            cur = cur.next
            cur1 = cur1.next
        cur.next = None  # Note 容易忘!
        return head1

if __name__ == '__main__':
    """
    解法1: 
        用字典记录之前的node. 
        第一遍只负责创建node并存入字典, 第二个循环负责next和random的指针. 
        坑:
            1. cur = cur.next
            2. 判断next和random是否为空...
    解法2:
        用字典, 但是one pass
        主要是定义了getnew函数, 缺啥补啥
    解法3: 
        在每个node后面又搞了一个node. 方便找位置. 
        先连next.
        再搞random: 注意这里必须判断是否为None
        然后split
        最后还要赋值None
    """
    s = Solution()
    print(s.copyRandomList(list2Node([[1,2], [2,2]])))

