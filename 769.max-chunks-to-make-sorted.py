#
# @lc app=leetcode id=769 lang=python
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hi = 0
        cnt = 0
        for i, n in enumerate(arr):
            hi = max(n, hi)
            if i == hi:
                cnt += 1
        return cnt

if __name__ == '__main__':
    """
    坑: 
        必须知道当前位置.. i hi n 三个指针比较. 
        必须先计算max, 用以处理初始化的情况...
    """
    s = Solution()
    print(s.maxChunksToSorted([4,3,2,1,0]))
# @lc code=end

