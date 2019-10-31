#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(nums)
        if not nums:
            return []
        if k == 1:
            return nums
        res = []
        deq = deque([])
        for idx, item in enumerate(nums):
            while deq and nums[deq[-1]] < item:  # 忘了nums..
                deq.pop()
            deq.append(idx)
            if deq[0] == idx - k:
                deq.popleft()
            if idx >= k -1:
                res.append(nums[deq[0]])  # 忘了nums...
        return res

if __name__ == '__main__':
    """
    题设: 
        对于长度为n的nums, 只能看到在滑窗内的 k 个数字。
        滑动窗口每次只向右移动一位。返回历次滑动窗口中的最大值。
    解法1: 优先队列 NlogK
    解法2: deque N
        核心思路是, 如果index在前面, 且数字值更小则一定用不到
        1. 先clean: 如果队列里有不如当前数字大的数, 则丢弃. (所以有序)
            因为有序性, 从最小的开始比较..
        2. 加入当前数到队列后面, 此时前面的都大于当前数, 
        3. 如果第一个数是i-k, 即已经越界, 丢弃
        4. 此时已经有序, 如果i扩招到第一个窗的大小, 开始放结果.
    解法3: DP TODO
    """
    s = Solution()
    # print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    print(s.maxSlidingWindow([7,2,4], 2))
    
# @lc code=end

