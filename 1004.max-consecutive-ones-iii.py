#
# @lc app=leetcode id=1004 lang=python
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        lo = 0
        res = 0
        cnt = 0
        for hi, item in enumerate(A, 1):  # [lo, hi)
            cnt += 1 - item  # 注意这个写法!
            if cnt <= K:
                res = max(res, hi - lo)
            else:
                while cnt > K:
                    cnt -= 1 - A[lo]
                    lo += 1
        return res

if __name__ == '__main__':
    """
    思路: 每一步找到以hi为结尾的最长序列, 滑动窗即可.
    """
    s = Solution()
    print(s.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
                    
# @lc code=end

