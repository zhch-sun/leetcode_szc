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
    #     cnt = list(Counter(s).items())  # Counter有个most_common是排好序的.
    #     cnt.sort(key=lambda x: x[1], reverse=True)
    #     return ''.join([x[0] * x[1] for x in cnt])
        
    #     res = ''  # 下面是一个连接字符串操作, +=和join速度差不多
    #     for key, num in count:
    #         res += key * num
    #     return res
    
    def frequencySort(self, s):
        N = len(s)
        bucket = [[] for _ in s]
        count = list(Counter(list(s)).items())  # Counter有个most_common是排好序的.
        for char, freq in count:
            bucket[-freq].append(char)
        res = ''
        for idx, item in enumerate(bucket):
            for char in item:
                res += (N - idx) * char
        return res


if __name__ == '__main__':
    """
    sort Or bucket sort
    """
    s = Solution()
    print(s.frequencySort("tree"))
    print(s.frequencySort("cccaaa"))
    print(s.frequencySort("Aabb"))


        
            
        

