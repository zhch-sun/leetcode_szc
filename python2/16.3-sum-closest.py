#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        nums.sort()
        N = len(nums)
        ans = float('inf')
        for i, n in enumerate(nums):  # 这里可以prune
            lo, hi = i + 1, N - 1
            while lo < hi:
                total = n + nums[lo] + nums[hi]
                ans = ans if abs(total - target) > abs(ans - target)\
                    else total
                if total < target:
                    lo += 1
                elif total > target:
                    hi -= 1
                else:
                    return ans
        return ans  # 一定有解. 不需判断

if __name__ == '__main__':
    """
    题设: return一个解
    解法1:
        应该判断len(nums)>3
        TODO pruning法？3*item-target>abs(target-closest)
        注意, 先判断 < > 最后判断=的写法最快? 不知为何.
    解法2:
        见最快的submission. 还是有prune的.
    """
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))

