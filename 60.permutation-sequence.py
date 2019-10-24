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
    题设: 给定n和k, 返回第k个排列
    题目思路:
        需要写一下1234的1的所有情况. 
        1的格数是234的permute也就是3! 
        所以divmod的商就是第一位的值, 余数是下一个k
        而且直接pop就可以, 下一次的idx还是正确的
    两种循环:
        while n: 正常思路, 可以str +=
        while k可以实现early stopping. k=0的时候只要按顺序把剩下的数字放进去即可
        这样最好用一个list暂存
    corner case:
        python 没有阶乘!  ...  只能math.factorial. 
        还有就是k和n的对齐. 因为k=1的时候对应是不选的, 所以k-=1!
    TODO 也可以先算出最终的阶乘，循环中每次除n? 这样应该可以大幅加速.
    TODO Note: 目前所有的做法都需要从一个list里面remove.要么就是平移所有的数..其实就是remove.
    """
    s = Solution()
    print(s.getPermutation(4,9))
