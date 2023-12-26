#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        ans = 0  # 处理空输入
        for n in nums:
            if n - 1 not in nums:
                cnt = 1
                while n + 1 in nums:
                    cnt += 1
                    n += 1
                ans = max(ans, cnt)
        return ans

if __name__ == '__main__':
    """
    题设: 
        无序整数数组, 找最长的连续上升序列. 
        4567算连续. 复杂度需要O(N)
    解法1: 
        先转化成set, 再循环
        只有 x - 1 不存在的时候, 才开始循环.. 
        这样可以避免重复操作. 使得最后就是o(n)
    解法2: 
        union find, 每输入一个数找相邻的两个数.. 也要set查找..
        还不如直接set.
    """
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
    
