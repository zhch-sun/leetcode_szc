#
# @lc app=leetcode id=451 lang=python
#
# [451] Sort Characters By Frequency
#
from collections import Counter
import itertools

class Solution(object):
    # def frequencySort(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     s = list(s)
    #     count = list(Counter(s).items())  # Counter有个most_common是排好序的.
    #     count.sort(key=lambda x: x[1], reverse=True)
        
    #     res = ''  # 下面是一个连接字符串操作, 应该还是+=最快.
    #     for key, num in count:
    #         res += key * num
    #     return res
    
    def frequencySort(self, s):
        N = len(s)
        bucket = [[] for _ in s]
        count = list(Counter(list(s)).items())  # Counter有个most_common是排好序的.
        for key, num in count:
            bucket[-num].append(key)
        res = ''
        for idx, item in enumerate(bucket):
            for i in item:
                res += (N - idx) * i
        return res


if __name__ == '__main__':
    """
    sort Or bucket sort
    """
    s = Solution()
    print(s.frequencySort("tree"))
    print(s.frequencySort("cccaaa"))
    print(s.frequencySort("Aabb"))


        
            
        

