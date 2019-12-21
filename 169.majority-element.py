#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]  # or count=0 major=None
        count = 1
        for i in range(1, len(nums)):  # 从1开始, 不能enumerate?
            if count + i - len(nums) > 0:  # my condition for terminate
                return major
            item = nums[i]
            if item == major:
                count += 1
            elif count > 0:
                count -= 1
            else:
                major = item  
                count += 1  # 这里应该是要的, 不加1也可以过测试..
        return major

if __name__ == '__main__':
    """
    题设: 求众数, 即输出次数大于⌊n/2⌋ 给定序列一定存在众数
    解法1: 可以sort取中值. 
    解法2: 
        摩尔投票法: 对拼消耗. 每次从序列中挑出两个不同的数字抵消掉. 剩下的就是
        先另第一个数为major. 计算major的数量. 
        可以early stopping! 目前没有公开答案想到. 即剩下的数还不如count多, 可以stop!
        即 count > len(nums) - i; 把元素放到一边, 另一边为0时更快..
        enumerate也不快
    解法3:
        quick selection取中位数. 
    """
    s = Solution()
    print(s.majorityElement([2,1,1,1,2,2]))
