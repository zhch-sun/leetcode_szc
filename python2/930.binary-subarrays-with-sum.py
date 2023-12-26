#
# @lc app=leetcode id=930 lang=python
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
from collections import Counter
from collections import defaultdict

class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """        
        # 动态计算前缀和
        psum, ans = 0, 0
        seen = defaultdict(int)
        seen[0] = 1
        
        for n in A:
            psum += n
            ans += seen[psum - S]
            seen[psum] += 1
        return ans

    # def numSubarraysWithSum(self, A, S):
    #     # 预计算前缀和
    #     ans = 0
    #     N = len(A)
    #     P = [0] * (N + 1)
    #     for idx, item in enumerate(A):
    #         P[idx + 1] = P[idx] + item

    #     seen = defaultdict(int)
    #     # seen[0] = 1
    #     for psum in P:
    #         ans += seen[psum - S]
    #         seen[psum] += 1
    #     return ans

if __name__ == '__main__':
    """
    解法1:
        不能双指针, 因为0010100, 前后构成了一个组合, 有多重情况
        可以三指针, 未写 
    解法2:
        还是前缀和简单易懂
    """
    s = Solution()
    print(s.numSubarraysWithSum([1,0,1,0,1], 2))
# @lc code=end

