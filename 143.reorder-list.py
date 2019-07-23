#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
#

def list2Node(input):
    dummy = ListNode(0)
    cur = dummy
    for item in input:
        cur.next = ListNode(item)
        cur = cur.next
    return dummy.next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        next = ',' + self.next.__repr__() if self.next else ''
        return str(self.val) + next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        slow, fast = head, head
        # 找到中点
        while fast and fast.next: # slow的位置是 (n + 1) // 2 # 从slow处reverse
            slow = slow.next
            fast = fast.next.next
        # # 这里应该把slow后面的拆下来?
        # head1 = slow.next
        # slow.next = None

        # 先在从slow后面reverse.
        node = slow.next
        # cur = node.next # the node to be reversed # 可能不存在...
        while node and node.next:
            cur = node.next
            outer = cur.next
            cur.next = slow.next
            slow.next = cur
            node.next = outer
            cur = outer  # node 不变
        
        cur = head
        while slow.next:
            node = slow.next
            outer = node.next
            node.next = cur.next
            cur.next = node
            slow.next = outer
            cur = node.next
        return head

    # def reorderList(self, head):
    #     if not head:
    #         return head
    #     # find the middle
    #     slow, fast = head, head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next 
    #     head1 = slow.next
    #     slow.next = None
    #     # reverse latter part
    #     pre = None  # pre是新生成的序列的头
    #     while head1:  # head去和pre换. 而不是head.next和pre换
    #         save = head1.next
    #         head1.next = pre
    #         pre = head1
    #         head1 = save
    #     # merge...
    #     cur = head
    #     while pre:
    #         node = pre
    #         outer = node.next
    #         node.next = cur.next
    #         cur.next = node
    #         pre = outer
    #         cur = node.next            
    #     return head


        
if __name__ == '__main__':
    """
    TODO 这道题写得太差了.. 感觉
    解法1: 也可以搞额外的dict存着...
    解法2: 1找中点, 2reverse后面, 3插入.. 如果中点不断, 就是92题
    解法3: 如果在找中点后面断开, reverse的写法更简单. 因为不需要保存最前面的链接了.206题.
        这样需要head和一个可能是fake的pre去不停交换. 
    """
    s = Solution()
    # print(s.reorderList(list2Node([1])))
    print(s.reorderList(list2Node([1,2,3,4,5])))
    print(s.reorderList(list2Node([1,2,3,4,5,6])))
