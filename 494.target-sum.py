#
# @lc app=leetcode id=494 lang=python
#
# [494] Target Sum
#
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """        
        # 40ms 99.58%
        total = sum(nums)
        target, remain = divmod(total - S, 2)
        if remain or total < S:  # Note 必须判断, 且不能=!
            return 0
        f = [0] * (target + 1)
        f[0] = 1
        curSum = 0
        for n in nums:
            curSum += n
            for j in xrange(min(target, curSum), n - 1, -1):  # 又忘了截止位置
                f[j] += f[j - n]
        return f[-1]

if __name__ == '__main__':
    """
    题设: 
        非负整数. 填正负号. 求总和为target得方案数. 
    解法1: 
        01背包
    解法2:
        两个优化, 未写. 
        sort, 过滤前面的0和后面的大于target的值, 因为最后面的一定是正的? 需要推导
        最后2**num0*f[-1]
    """
    s = Solution()
    print(s.findTargetSumWays([1], 1))
    print(s.findTargetSumWays([1, 0], 1))
    print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(s.findTargetSumWays([1,2,7,9,981], 1000000000000))
