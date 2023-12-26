#
# @lc app=leetcode id=719 lang=python
#
# [719] Find K-th Smallest Pair Distance
#
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def count(nums, mid, N):
            # 这个和378的模板一样
            j = 0  # 1亦可
            cnt = 0
            for i in xrange(N):  # 替换原先的while, 快了一些
                while j < N and nums[j] - nums[i] <= mid:
                    j += 1  # j = 1的时候没有元素..
                cnt += j - i - 1  # 实际是一个上三角矩阵
            return cnt
            
        N = len(nums)
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:  # [lo, hi]
            mid = lo + (hi - lo) // 2
            cnt = count(nums, mid, N)
            if cnt < k:
                lo = mid + 1
            else:
                hi = mid
        return lo
        
if __name__ == '__main__':
    """
    题设: 
        给定一个整数数组，返回所有数对之间的第 k 个最小距离。
        一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。
    解法:
        仍然是注意count函数
    """
    s = Solution()
    print(s.smallestDistancePair([1,3,1], 1))

