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
#         # Note 直接修改的话顺序不变, 需要先删除
#         value = self.cache[key]
#         self.cache.pop(key)
#         self.cache[key] = value
#         return self.cache[key]

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         if key in self.cache:
#             self.cache.pop(key)   # Note 必须先删除!
#         if len(self.cache) == self.capacity:
#             # 注意接口. 只有两头可以pop, popitem函数     
#             self.cache.popitem(last=False) 
#         self.cache[key] = value

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.top = Node(None, None)
        self.bot = Node(None, None)
        self.top.prev = self.bot  # top为最常用
        self.bot.next = self.top
        self.cache = {}  # {key: node}

    def _add(self, node):  # 在链表头上插入..
        p, n = self.top.prev, self.top
        p.next = node
        node.prev = p
        node.next = n
        n.prev = node

    def _remove(self, node):  # 从链表中删除
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]    
        self._remove(node)  # dict是不变的.
        self._add(node)   
        return node.val       

    def put(self, key, value):
        if self.capacity == 0:  # Note 处理corner case!
            return
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                node = self.bot.next
                self._remove(node)
                self.cache.pop(node.key, None)  # 这里也要删除.             
            node = Node(key, value)
            self.cache[key] = node
            self._add(node)   
            return
        else:          
            node = self.cache[key] 
            node.val = value  # Note 必须重新赋值   
            self.get(node.key)  # 这里get
            return

if __name__ == '__main__':
    """
    解法1: 
        用ordereddict实现. 注意先删除再赋值和popitem.
        python2里这个本身就是用dict+双向链表来做的. 
        速度比手写更慢
    解法2: 
        dict + 双向链表(两个dummy)
        dict里面存着双向链表的node, node里存key和value
        双向链表一样需要赋值大法进行操作.
        细节: 
            put不能调用get, get返回的-1可能是value的值
            put时即使key存在也要重新赋值
            remove和add不仅有node操作, 还有cache操作
        抽象:
            还是抽象成remove和add比较合理... 且输入为node. 
            popleft和move_to_end应该是更高层的抽象...
    """
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

