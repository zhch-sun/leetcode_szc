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
        # 居然只有80%
        nums = set(nums)
        res = 0
        for x in nums:
            if x - 1  not in nums:
                y = x + 1
                # cur = 1
                while y in nums:
                    y += 1
                    # nums.remove(y)  # 这是不可以的!! 循环中不能改变nums
                    # cur += 1
                res = max(y - x, res)
        return res
        
    # def longestConsecutive(self, nums):
    #     nums = set(nums)
    #     res = 0
    #     while nums:  # set 
    #         x = nums.pop()
    #         if x - 1 not in nums:
    #             y = x + 1
    #             while y in nums:
    #                 nums.remove(y)
    #                 y += 1
    #             res = max(res, y - x)
    #         else:
    #             nums.add(x)
    #     return res        

if __name__ == '__main__':
    """
    解法1: 答案先转化成set, 非常巧妙.
        只有 x - 1 不存在的时候, 才开始循环.. 这样可以避免重复操作. 使得最后就是o(n)
    解法2: union find
        还是要把输入转换成(num,i) 的dict, 并查集的array大小是 nums的长度...
    解法3: 错解... set不是queue, 不能这么搞..
    TODO union find什么鬼?
    """
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
    
