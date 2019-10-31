#
# @lc app=leetcode id=739 lang=python
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 这题对T append 0 是没有用的
        res = [0] * len(T)  # 必须初始化!!! 且用0初始化, 不能None
        stack = []  
        for idx, item in enumerate(T):
            while stack and item > T[stack[-1]]:
                pre = stack.pop()
                res[pre] = idx - pre  # Note 忘记-pre了.....
            stack.append(idx)
        return res

if __name__ == '__main__':
    """
    题设: 找所有位置下一个温升时刻
    解法: 维护一个递减单调栈, 找右边第一个大于它的数
    坑: 是未来有几天, 是个相对值.......
    """
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
# @lc code=end

