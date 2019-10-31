#
# @lc app=leetcode id=503 lang=python
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        res = [-1] * N
        stack = []
        for idx in range(2 * N):  # Note
            item = nums[idx % N]  # Note
            while stack and item > nums[stack[-1]]:
                pre = stack.pop()
                res[pre] = item
            stack.append(idx % N)  # Note
        return res

if __name__ == '__main__':
    """
    题设: 
    解法: 循环数组: 循环边界, item取值, stack赋值, 都要处理
    """
    s = Solution()
    print(s.nextGreaterElements([1,2,1]))
# @lc code=end

