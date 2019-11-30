#
# @lc app=leetcode id=460 lang=python
#
# [460] LFU Cache
#

# @lc code=start
from collections import defaultdict, OrderedDict
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key2node = {}
        self.freq2list = defaultdict(OrderedDict)
        self.capacity = capacity
        self.minf = 0
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1
        key, value, freq = self.key2node[key]
        self.freq2list[freq].pop(key)
        self.key2node.pop(key)
        if not self.freq2list[freq] and freq == self.minf:
            self.minf += 1
        node = [key, value, freq + 1]
        self.key2node[key] = node
        self.freq2list[freq + 1][key] = node  # 忘记key..
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:  # corner case...
            return
        if key not in self.key2node:
            if len(self.key2node) == self.capacity:
                del_key, _ = self.freq2list[self.minf].\
                    popitem(last=False)
                self.key2node.pop(del_key)
            node = [key, value, 1]  # Note 需要改freq, 只能list
            self.key2node[key] = node
            self.freq2list[1][key] = node  # Note 忘记key..
            self.minf = 1
        else:
            self.key2node[key][1] = value  # Note 不改freq!
            self.get(key)  # Note 用get(key)!!!
        
if __name__ == '__main__':
    """
    解法1: 
        1. key到node的映射 key2node {} 
        2. freq到nodeList的映射 defaultdict(OrderedDict)
        3. 还要维护当前最小的freq...
        坑:
            1. self.freq2list[1][key]很容易忘记写key...
            2. put里面调用get最方便
            3. node只能list, 因为要改freq
            4. capacity == 0...
        但是会慢
    解法2: 
        实际最快.
        用一个变量rank记录key加入的时间, 然后用优先队列可以双重排序! 
        但是优先队列的复杂度是log(N)
        1. key到node的映射 cache {}
        2. 优先队列pq, 里面是[freq, rank, key, value]
    """
    cache = LFUCache(2)
    print(cache.put(1, 1))
    print(cache.put(2, 2))
    print(cache.get(1)   )    # returns 1
    print(cache.put(3, 3))   # evicts key 2
    print(cache.get(2)   )    # returns -1 (not found)
    print(cache.get(3)   )    # returns 3.
    print(cache.put(4, 4))    # evicts key 1.
    print(cache.get(1)   )    # returns -1 (not found)
    print(cache.get(3)   )    # returns 3
    print(cache.get(4)   )    # returns 4    

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



