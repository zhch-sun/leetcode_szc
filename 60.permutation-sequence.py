#
# @lc app=leetcode id=60 lang=python
#
# [60] Permutation Sequence
#
import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = list(range(1, n + 1))
        k -= 1
        while k:
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            res.append(nums[idx])
            nums.pop(idx)
        
        res += nums
        return ''.join(map(str, res))

    # def getPermutation(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: str
    #     """
    #     res = ''
    #     nums = map(str, range(1, n + 1))
    #     k -= 1
    #     while n:
    #         n -= 1
    #         idx, k = divmod(k, math.factorial(n))
    #         res += nums[idx]
    #         nums.pop(idx)
    #     return res
        
if __name__ == '__main__':
    """
    python 没有阶乘!  ...  只能math.factorial. 
    还有就是k和n的对齐. 因为k=1的时候对应是不选的, 所以k-=1!
    也可以预先用一个数列存着0-n的阶乘，或者算出最终的阶乘，循环中每次除ｎ．
    while k的时候, 可以early stopping.
    while n的时候, 可以先生成一个字符串.
    Note: 目前所有的做法都需要从一个list里面remove. 要么就是平移所有的数..其实就是remove.
    """
    s = Solution()
    print(s.getPermutation(4,9))
