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
    #     # 99.7%
    #     # 还是不写这个了...
    #     if not head:
    #         return None
    #     cur = head
    #     tmp = {}
    #     prev = None  # the previous second node
    #     while cur is not None:
    #         sec = Node(cur.val, None, None)  # the copied node
    #         tmp[cur] = sec
    #         if prev is not None:
    #             prev.next = sec
    #         else:
    #             head2 = sec
    #         prev = sec  # 这里也太难了.
    #         cur = cur.next
        
    #     cur = head
    #     while cur is not None:
    #         sec = tmp[cur]
    #         if cur.random is not None:
    #             sec.random = tmp[cur.random]  #天呐这个顺序..
    #         cur = cur.next

    #     return head2

    # def copyRandomList(self, head):
    #     if not head:
    #         return head
    #     cur = head
    #     tmp = {}
    #     while cur is not None:
    #         tmp[cur] = Node(cur.val, None, None)
    #         cur = cur.next
    #     cur = head
    #     while cur is not None:
    #         if cur.next is not None:
    #             tmp[cur].next = tmp[cur.next]
    #         if cur.random is not None:
    #             tmp[cur].random = tmp[cur.random]  # Note 容易错呀
    #         cur = cur.next
    #     return tmp[head] #Note 没有dummyle.

    def copyRandomList(self, head):
        if not head:
            return head
        # copy after the position
        cur = head
        while cur is not None:
            save = cur.next
            node = Node(cur.val, None, None)
            cur.next = node
            node.next = save
            cur = save
        # set random
        cur = head
        while cur is not None:  #一定是偶数
            sec = cur.next
            if cur.random is not None:
                sec.random = cur.random.next
            cur = sec.next
        # split the list node
        head0 = head  # head of the original list
        cur = head1 = head.next  # 从head.next开始!!
        while cur.next:  # 这里写cur.next!
            head.next = cur.next
            head = head.next
            cur.next = cur.next.next
            cur = cur.next # 这里cur.next就行了..
        head.next = None # 回复到原来的list.
        return head1


if __name__ == '__main__':
    """
    第一种解法: 这题应该不需要dummy head. TODO 理解什么时候需要dummy. 
        第一遍需要记录sec的prev? 有什么更好的方法吗? 
    第二种解法: 第一遍只负责copy, 第二个循环负责next和random的指针. 
        这个算法简洁得多
    第三种解法: 在每个node后面又搞了一个node. 
        注意这个copy之后, 不能同时连next和random? 需要分两步走
        而且原list是不能改变的
    """
    s = Solution()
    print(s.copyRandomList(list2Node([[1,2], [2,2]])))

