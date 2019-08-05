#
# @lc app=leetcode id=165 lang=python
#
# [165] Compare Version Numbers
#
class Solution(object):
    # def compareVersion(self, version1, version2):
    #     """
    #     :type version1: str
    #     :type version2: str
    #     :rtype: int
    #     """
    #     l1 = map(int, version1.split('.'))
    #     l2 = map(int, version2.split('.'))
    #     n = max(len(l1), len(l2))
    #     for i in range(n):
    #         if i < len(l1) and i < len(l2):
    #             x1, x2 = l1[i], l2[i]
    #             if x1 < x2:
    #                 return -1
    #             elif x1 > x2:
    #                 return 1
    #         else:
    #             if i < len(l1):
    #                 x = sum(l1[i:])
    #                 if x > 0:
    #                     return 1
    #                 else:
    #                     return 0
    #             elif i < len(l2):
    #                 x = sum(l2[i:])
    #                 if x > 0:
    #                     return -1
    #                 else:
    #                     return 0                    
    #     return 0

    # def compareVersion(self, version1, version2):
    #     l1 = map(int, version1.split('.'))
    #     l2 = map(int, version2.split('.'))
    #     n = max(len(l1), len(l2))
    #     for i in range(n):
    #         x1 = l1[i] if i < len(l1) else 0
    #         x2 = l2[i] if i < len(l2) else 0
    #         if x1 < x2:
    #             return -1
    #         elif x1 > x2:
    #             return 1
    #     return 0
        
    def compareVersion(self, version1, version2):
        from itertools import izip_longest
        l1 = map(int, version1.split('.'))
        l2 = map(int, version2.split('.'))
        for x1, x2 in izip_longest(l1, l2, fillvalue=0):
            if x1 < x2:
                return -1
            elif x1 > x2:
                return 1
        return 0

if __name__ == '__main__':
    """
    主要难点在于处理不同长度的 nums
    解法1:
        当一个结束之后, 对另一个剩下的部分求和. 因为不存在负数, 所以很好判断.
    解法2:
        给如果不够长则直接赋值默认的0. 代码更短. 
    解法3:
        python的itertools有izip_longest, 可以自动fill0..
    """
    s = Solution()
    print(s.compareVersion('0.1', '1.1'))
    print(s.compareVersion('1', '1.0'))
    print(s.compareVersion('1.1', '1'))
