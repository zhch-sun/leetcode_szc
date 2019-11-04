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
        for i in xrange(2 * N):  # Note
            n = nums[i % N]  # Note
            while stack and n > nums[stack[-1]]:
                pre = stack.pop()
                res[pre] = n
            stack.append(i % N)  # Note
        return res

if __name__ == '__main__':
    """
    题设: 
    解法1: 
        循环数组: 循环边界, item取值, stack赋值, 都要处理
    解法2:
        可以利用max prune, 不写. 
        用deque清空不需要的值? 需要吗? 可能不需要. 
    """
    s = Solution()
    print(s.nextGreaterElements([1,2,1]))
# @lc code=end

