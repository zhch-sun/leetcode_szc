#
# @lc app=leetcode id=84 lang=python
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]  # 需要-1处理栈中只有1个数且被pop的情况
        heights.append(0)  # 最后加0可以确保数组中均被处理
        ans = 0
        for i, h in enumerate(heights):
            while len(stack) > 1 and h < heights[stack[-1]]:  # Note len>1!
                pre = stack.pop()  # index
                dist = i - stack[-1] - 1  # Note not idx-pre, idx-stack[-1]
                ans = max(ans, heights[pre] * dist)
            stack.append(i)
        heights.pop(0)  # Note 最好还是加上!
        return ans

    # def largestRectangleArea(self, heights):
    #     stack = [-1]  # 需要-1处理栈中只有1个数且被pop的情况
    #     # heights.append(0)  # 最后加0可以确保数组中均被处理
    #     area = 0
    #     for idx, item in enumerate(heights):
    #         while len(stack) > 1 and item < heights[stack[-1]]:
    #             area = max(area, heights[stack.pop()] * (idx - stack[-1] - 1) )
    #         stack.append(idx)
    #     while len(stack) > 1:  # 不用尾sentinel的写法
    #         area = max(area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
    #     return area
  
if __name__ == '__main__':
    """
    题设: 
        给定n个非负整数，用来表示柱状图中各个柱子的高度。
        求在该柱状图中，能够勾勒出来的矩形的最大面积。
    解法1: 单调栈
        只想到了如下理解方式:
            分别考虑 完整包含第i个矩形的最大面积, 
            最终解是i个值中的最大值.
            面积的计算: 延伸到两边第一个小于第i个巨型高度的位置.
        优秀图解: 
            https://blog.csdn.net/Zolewit/article/details/88863970
        tricks:
            实质上需要两边+0, 操作上: 
            1. stack最前面添加一个-1, 处理第一个数被pop的情况
            2. heights最后加个0, 确保数组均被处理.
    解法2: 
        没有其他更好解法, 写一个不用尾sentinel
    """
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))    
# @lc code=end

