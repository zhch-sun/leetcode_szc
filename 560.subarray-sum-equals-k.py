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
        cumsum = 0
        cnt = 0
        d = defaultdict(int)  # 注意初始化
        d[0] = 1  # 不是针对[], 而是针对cumsum == k

        for n in nums:
            cumsum += n
            cnt += d[cumsum - k]  #顺序不能调换
            d[cumsum] += 1  # 计算cnt
        return cnt
            
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
    print(s.subarraySum([1], 0))
# @lc code=end

