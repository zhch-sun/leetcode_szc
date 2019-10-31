#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
# class MonoStack(object):  
#     # min monostack
#     def __init__(self, nums):
#         self.s = []
#         self.a = nums
#         self.cnt = 0

#     def push(self, x):
#         while self.s and self.a[self.s[-1]] < self.a[x]:
#             self.a.pop()
#         self.s.append(x)

#     def min(self):
#         return self.s[-1] if self.s else -1

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []  # 存储index. 因为需要水槽的横向长度
        cnt = 0
        # 每一步都得出以当前idx为结尾的水量的正确值
        for idx, item in enumerate(height):  # 下面在分类讨论item
            # 尽管是while stack, 但是只有len(stack) >= 2 才有解
            while stack and item > height[stack[-1]]:  # Note stack为空!
                low = height[stack.pop()]  # 容易忘记height
                if not stack:
                    break
                dist = idx - stack[-1] - 1
                diff = min(item, height[stack[-1]]) - low
                cnt += dist * diff
            # 上面的循环有三个跳出条件, stack空, item<=, stack空
            # 而且必须先while后面跟append.. 反过来的写法很复杂...
            stack.append(idx)  # Note 等于的情况也要push!
        return cnt

if __name__ == '__main__':
    """
    题目:  
        非负整数表示高度, 求能够接的总雨水的和. 
        注意: 不是求最大能接水的槽!!!
    分析:
        当从左向右扫描时, 假设当前块是已知的最大值, 
        则左边的形状对右边蓄水的计算无影响.
    解法1: 单调栈
        每一个水槽由递减区间和递增区间组成. 最少需要三个数字构成槽. 
        假设不考虑连续的相同数字, 则总是三个数字开始计算. 
        即在从左向右循环的过程中, 从下向上累计水. 
        方法是: 
            pop出最低值, 保留左边界. 
            最低值相当于雨水空间的下界.
            对于右边界
                如果=左边界, 需要压栈! 表明左右边界中间已经没有坑了! 
                    否则后面如果接了一个更小的会多算. 
                如果<左边界, 可能构成未来的最低点, 需要压栈.
                如果大于左边界, 需要把原先的左边界pop, 直到左边的都大于他
                即一个正常的minstack的操作.
        总体架构: 
            for循环里分类讨论item与left大小的三种情况
    解法2:
        TODO 双指针. 
    解法3:
        TODO dp 
    """
    s = Solution()
    # print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6 
    print(s.trap([5,2,1,2,1,5]))  # 14
# @lc code=end

