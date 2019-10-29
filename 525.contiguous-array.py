#
# @lc app=leetcode id=525 lang=python
#
# [525] Contiguous Array
#

# @lc code=start
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        s = 0  # current sum
        res = 0
        d[0] = -1  # cumsum的起始位都是很特殊的
        for idx, n in enumerate(nums):
            s += 1 if n else -1
            if s in d:
                res = max(res, idx - d[s])  # Note 这里不加1!
            else:
                d[s] = idx
        return res

if __name__ == '__main__':
    """
    只要存起始位置就可以. 不需要存两个数
    cumsum的起始位还是一个特殊处理. 
    """
    s = Solution()
    print(s.findMaxLength([0,1]))
    print(s.findMaxLength([0,1,0]))
# @lc code=end

