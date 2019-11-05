#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#

class Solution(object):
    # def lengthOfLIS(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """        
    #     if not nums:
    #         return 0
    #     N = len(nums)
    #     f = [0] * N
    #     for i in xrange(N):
    #         f[i] = 1
    #         for j in xrange(i):  # 0 没有进入下面的循环
    #             if nums[i] > nums[j]:
    #                 f[i] = max(f[i], f[j] + 1)
    #     return max(f)  # 忘记了..

    # def lengthOfLIS(self, nums):
    #     if not nums:
    #         return 0
    #     N = len(nums)
    #     f = [1] * N
    #     for i in xrange(N):
    #         for j in xrange(i):  # 0 没有进入下面的循环
    #             if nums[i] > nums[j]:  # 根据题设也可以取等号. 
    #                 f[i] = max(f[i], f[j] + 1)
    #     return max(f) # 仍然需要判断是否空nums
    
    # def lengthOfLIS(self, nums):
    #     N = len(nums)
    #     f = [0] * N
    #     ans = 0
    #     for n in nums:
    #         lo, hi = 0, ans   # hi是不被包含的!
    #         while lo < hi:  # [lo, hi]
    #             mid = lo + (hi - lo) // 2
    #             if f[mid] < n:  # Note 不是nums, 
    #                 lo = mid + 1
    #             else:
    #                 hi = mid  # 三种讨论的二分速度更快. 
    #         f[lo] = n
    #         if lo == ans:  # Note 也容易写错, ans是取不到的.
    #             ans += 1
    #     return ans

    def lengthOfLIS(self, nums):
        N = len(nums)
        f = [0] * N
        ans = 0
        for n in nums:
            lo, hi = 0, ans   # hi是不被包含的!
            while lo < hi:  # [lo, hi]
                mid = lo + (hi - lo) // 2
                if f[mid] < n:  # Note 不是nums, 
                    lo = mid + 1
                elif f[mid] > n:
                    hi = mid  
                else: 
                    lo = hi = mid  # 三种讨论的二分速度更快.
            f[lo] = n
            if lo == ans:  # Note 也容易写错, ans是取不到的.
                ans += 1
        return ans

if __name__ == '__main__':
    """
    题设: 最长上升子序列. 不含相等元素/严格上升. 
    解法1:
        DP, 需要注意主循环后的赋值位置. 
        注意最后返回最大值!!!
        修改1:
            DP, 全部初始化成1, 不需要中间的赋值. 
    解法2:
        二分, 学名patience sorting, 需要很多证明
        https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
        https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
        
        维护一个列表tails，其中每个元素tails[k]的值代表 
        长度为k+1的子序列尾部元素, 当前的最小值。
        列表一定严格递增. 

        二分居然写错了!!
    解法3: 
        三种讨论的二分更快
    """
    s = Solution()
    print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
    print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6]))
