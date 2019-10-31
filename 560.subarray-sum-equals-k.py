#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        psum, ans = 0, 0
        seen = defaultdict(int)
        seen[0] = 1  # 不是针对[], 而是针对psum==0的情况
        for n in nums:
            psum += n
            ans += seen[psum - k]  # Note psum与k顺序
            seen[psum] += 1   # Note 与上面不能调换, 只有k==0的时候会触发错误
        return ans
            
if __name__ == '__main__':
    """
    题设: 返回该数组中和为k的连续的子数组的个数。存在负数
    解法:
        存在负数所以不能双指针
        思路是cumsum + hash. 
        array区间和是cumsum[hi] - cumsum[lo] == k
    坑: 
        必须初始化d[0]=1. 针对的情况是sum==k. 依赖于之前的0的个数
            比如[1,1,1,1], 4. 
        defaultdict就不要用get了, 即使用get也要显式写初值
        cnt更新必须在d更新前面
    """
    s = Solution()
    print(s.subarraySum([1,1,1], 2))
    print(s.subarraySum([1,2,3], 3))
    print(s.subarraySum([1,1,2,2,3], 3))
    print(s.subarraySum([1,1,1], 0))
# @lc code=end

