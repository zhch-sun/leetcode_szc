#
# @lc app=leetcode id=930 lang=python
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
from collections import Counter
class Solution(object):
    # def numSubarraysWithSum(self, A, S):
    #     """
    #     :type A: List[int]
    #     :type S: int
    #     :rtype: int
    #     """
    #     N = len(A)
    #     P = [0] * (N + 1)
    #     for idx, item in enumerate(A):
    #         P[idx + 1] = P[idx] + item

    #     cnt = Counter()
    #     ans = 0
    #     for item in P:
    #         ans += cnt[item - S]  # 注意是item-S
    #         cnt[item] += 1  # TODO 顺序???
    #     return ans
    
    def numSubarraysWithSum(self, A, S):
        cnt = Counter({0: 1})
        ans, psum = 0, 0
        for item in A:
            psum += item
            ans += cnt[psum - S]
            cnt[psum] += 1
        return ans


if __name__ == '__main__':
    """
    解法1:
        不能双指针, 因为0010, lo不是单调的运动. 
        不需要额外初始化..
    解法2:
        又是这个奇怪的初始化. cnt[0] = 1
    """
    s = Solution()
    print(s.numSubarraysWithSum([1,0,1,0,1], 2))
# @lc code=end

