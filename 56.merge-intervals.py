#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 98.24%
        if not intervals:
            return []
        intervals.sort(key=lambda item: item[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            item = intervals[i]
            if res[-1][1] >= item[0]:
                res[-1][1] = max(item[1], res[-1][1])  # 不需要整个改res[-1]
            else:
                res.append(item)
        return res

if __name__ == '__main__':
    """
    给定一堆区间, 合并其中重叠的.
    sort 添加函数的写法.
    Note 注意还有可能出现一个完全在另外一个里的情况! corner case呀
    解法2: 可以让res初始化为[], 但是这样就要在for循环里每次都要判断out是否为空. 不优雅.
    """
    s = Solution()
    print(s.merge([[2,6],[1,3],[8,10],[15,18]]))
    print(s.merge([[1,4],[4,5]]))
