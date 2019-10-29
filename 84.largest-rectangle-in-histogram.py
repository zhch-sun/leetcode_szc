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
        area = 0
        for idx, item in enumerate(heights):
            while stack and item < heights[stack[-1]]:
                area = max(area, heights[stack.pop()] * (idx - stack[-1] - 1) )
            stack.append(idx)
        return area
        
if __name__ == '__main__':
    """
    题设: 
        给定n个非负整数，用来表示柱状图中各个柱子的高度。
        每个柱子彼此相邻，且宽度为1。
        求在该柱状图中，能够勾勒出来的矩形的最大面积。
    解法1: 单调栈
        假设有n个矩形, 分别考虑第i个矩形, 求完整包含i的最大面积.
        这n个最大面积的最大值就是解.
        完整包含矩形i最大面积的求法: 
            https://blog.csdn.net/Zolewit/article/details/88863970
            对于任何一个矩形, 找到左右两边第一个小于它的值,
            中间部分乘以距离就是解
        所以计算过程中, 小的值未来是有用的.
        tricks:
            stack最前面添加一个-1, 处理第一个数被pop的情况
            heights最后加个0, 确保数组均被处理.
    """
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))    
# @lc code=end

