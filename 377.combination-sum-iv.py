#
# @lc app=leetcode id=377 lang=python
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        f = [0] * (target + 1)
        f[0] = 1
        for i in xrange(1, target + 1):
            for n in nums:
                if i >= n:
                    f[i] += f[i - n]
        return f[-1]

if __name__ == '__main__':
    """
    TODO 需要对这道题加深理解.
    f[j] = f[j-n[0]] + f[j-n[1]] + ... f[j-n[n-1]]
    非常漂亮的图解
    https://leetcode-cn.com/problems/combination-sum-iv/solution/dong-tai-gui-hua-python-dai-ma-by-liweiwei1419/
    """
    s = Solution()
    print(s.combinationSum4([1, 2, 3], 4))
        
# @lc code=end

