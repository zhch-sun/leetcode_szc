#
# @lc app=leetcode id=525 lang=python
#
# [525] Contiguous Array
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        psum, ans = 0, 0
        seen = defaultdict(int)
        seen[0] = -1
        for idx, n in enumerate(nums):
            psum += 1 if n else -1
            if psum in seen:
                ans = max(ans, idx - seen[psum])
            else:
                seen[psum] = idx
        return ans

if __name__ == '__main__':
    """
    题设: 
        给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）
    思路:
        把0转化成-1, 这样就可以用psum了...
    解法1:
        只要存每个psum的最开始位置
        起始位根据计算index需要是-1. 
        dict用in不要用get, 速度更快更易读
    """
    s = Solution()
    # print(s.findMaxLength([0,1]))
    # print(s.findMaxLength([0,1,0]))
    print(s.findMaxLength([0,0,1]))
# @lc code=end

