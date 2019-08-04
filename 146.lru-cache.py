#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#
from collections import OrderedDict

# class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.cache = OrderedDict()
#         self.capacity = capacity

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         if key not in self.cache:
#             return -1
#         # move key value to the end by delete and insert
#         # 直接修改的话顺序不变
#         value = self.cache[key]
#         del(self.cache[key])
#         self.cache[key] = value
#         return self.cache[key]

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if key in self.cache:
#             # self.cache[key] = value # Note 错了. 必须先删除, 再添加. 否则顺序不变
#             del self.cache[key]
#         if len(self.cache) + 1 > self.capacity:  # note this +1....
#             self.cache.popitem(last=False)  # 注意接口. 只有两头可以pop. # 不会删除key. 
#         self.cache[key] = value  

class Node(object):
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            del self.cache[key]

        if len(self.cache) > self.capacity - 1:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]

        n = Node(key, value)
        self._add(n)
        self.cache[key] = n
    
    def _remove(self, node):
        # 从链表中remove, 但是不删除元素, 也不处理dict对应的key value
        p = node.prev
        n = node.next  # 这个在只有一个元素的时候是None...
        p.next, n.prev = n, p

    def _add(self, node):
        # 在最后面add一个值.
        cur_tail = self.tail.prev
        cur_tail.next = node
        node.prev = cur_tail
        node.next = self.tail
        self.tail.prev = node        


if __name__ == '__main__':
    """
    解法1: 用ordereddict实现. python2里这个本身就是用dict+双向链表来做的. 
    解法2: dict + 双向链表
        dict里面存着双向链表的node
        node里面必须同时存key和val,否则在pop的时候无法删除dict中对应的元素..
        所以双向链表需要两个dummy...
        而且还要注意remove和add不仅有node操作, 还有cache操作...
        还是抽象成remove和add比较合理... popleft和move_to_end应该是更高层的抽象...
    """
    # cache = LRUCache(2)
    # cache.put(2, 2)
    # print(cache.get(2)) 
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
