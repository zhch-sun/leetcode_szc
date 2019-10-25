#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findPos(nums, target):
            left, mid = 0, 0
            for item in nums:
                if item < target:
                    left += 1
                elif item == target:
                    mid += 1
                    if mid >= 2:
                        return 0
            return -1 if left > target - 1 else 1

        N = len(nums) - 1
        lo, hi = 1, N
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if findPos(nums, mid) == 0:
                return mid
            elif findPos(nums, mid) == -1:
                hi = mid - 1
            else:
                lo = mid + 1
                
if __name__ == '__main__':
    """
    题设:
        整数数列长度为N+1, 里面整数的范围是1,N
        只有一个重复数, 找到它. 数字可能重复多次. 
        额外条件: 不准修改数列, 不准用额外空间
    坑:
        最小的输入是[1,1], 解的范围是[1, N]
    解法1: 二分. nlog(N)
        每个数统计一下左右两边的数量, 来确定解在哪边.
        findPos函数只需要统计<和=情况就可以了... 不需要>情况
    解法2:
        类似quick select, 可以O(N)?!
        是的, 但是不准修改数列
    解法3: TODO 
        cycle detection
    """
    s = Solution()
    print(s.findDuplicate([1,3,4,2,2]))
# @lc code=end

