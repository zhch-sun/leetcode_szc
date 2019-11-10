#
# @lc app=leetcode id=983 lang=python
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
class Solution(object):
    # def mincostTickets(self, days, costs):
    #     """
    #     :type days: List[int]
    #     :type costs: List[int]
    #     :rtype: int
    #     """
    #     def dfs(i):
    #         if i in f:
    #             return f[i]
    #         if i < 1:
    #             return 0
    #         if i not in days:
    #             return dfs(i - 1)
    #         # list comprehension真的是快很多
    #         f[i] = min(dfs(i - d) + c for d, c in zip(lasts, costs))
    #         return f[i]
    #     f = {}
    #     days = set(days)  # 在i not in days里面还有加速的功能! 
    #     lasts = [1, 7, 30]
    #     return dfs(365)

    # def mincostTickets(self, days, costs):
    #     def dfs(i):  # i是指days的索引. 
    #         if i >= N:
    #             return 0
    #         if i in f:
    #             return f[i]
    #         f[i] = float('inf')
    #         j = i  # Note 两重循环中j一直在增长!
    #         for d, c in zip(lasts, costs):
    #             while j < N and days[j] < days[i] + d:
    #                 j += 1
    #             f[i] = min(f[i], dfs(j) + c)  # Note 这一句不用在循环里..
    #         return f[i]

    #     list(set(days)).sort()
    #     N = len(days)
    #     lasts = [1, 7, 30]
    #     f = {}
    #     return dfs(0)  # i 是第i个日期.

    # def mincostTickets(self, days, costs):
    #     # 是解法1的bottom up版本
    #     maxDay = days[-1]
    #     days = set(days)  # 在i not in days里面还有加速的功能! 
    #     lasts = [1, 7, 30]
    #     f = [0] * (maxDay + 1)
    #     for i in xrange(1, maxDay + 1):
    #         if i not in days:  # 忘记这里了..
    #             f[i] = f[i - 1]
    #         else: # Note: else c很精髓! i-d==0有三种情况, 都是c !!!
    #             f[i] = min((f[i - d] + c if i - d > 0 else c)\
    #                 for d, c in zip(lasts, costs))
    #     return f[-1]

    # def mincostTickets(self, days, costs):
    #     # 解法2的bottom up版本, 
    #     # 也可以用queue, 需要更多空间, 但是更快.
    #     list(set(days)).sort()
    #     N = len(days)
    #     lasts = [1, 7, 30]
    #     f = [0] * N
    #     for i in xrange(N - 1, -1, -1):
    #         j = i
    #         f[i] = float('inf')
    #         for d, c in zip(lasts, costs):
    #             while j < N and days[j] < days[i] + d:
    #                 j += 1  # 这里可以用queue加速
    #             f[i] = min(f[i], (f[j] + c) if j < N else c)
    #     return f[0]
                
    def mincostTickets(self, days, costs):
        # 解法5
        from collections import deque
        list(set(days)).sort()
        dq7 = deque()  # 里面必须存一个pair
        dq30 = deque()
        ans = 0
        for d in days:
            while dq7 and dq7[0][0] + 7 <= d:
                dq7.popleft()
            while dq30 and dq30[0][0] + 30 <= d:
                dq30.popleft()
            dq7.append((d, ans))
            dq30.append((d, ans))
            ans = min(ans + costs[0], dq7[0][1] + costs[1], \
                dq30[0][1] + costs[2])
        return ans

    # def mincostTickets(self, days, costs):
    #     # 解法6
    #     list(set(days)).sort()
    #     N = len(days)
    #     f = [[] for _ in xrange(N)]
    #     p7, p30, p = 0, 0, 0
    #     ans = 0
    #     for d in days:
    #         while p7 != p and f[p7][0] + 7 <= d:
    #             p7 += 1
    #         while p30 != p and f[p30][0] + 30 <= d:
    #             p30 += 1
    #         f[p] = (d, ans)
    #         p += 1
    #         ans = min(ans + costs[0], f[p7][1] + costs[1], \
    #             f[p30][1] + costs[2])
    #     return ans

if __name__ == '__main__':
    """
    坑:
        记忆化时, 转移方程的f都要变成函数调用. 
    解法1: O(365)
        状态: 令f[i]为从0到第i日需要总价, 只考虑f[i]日旅行
        状态转移: f[i] = min(f[i-1] + c0, f[i-7] + c1, f[i-30] + c2)
        初始化: 空
        返回值: dfs(365)
    解法2: O(N)
        状态: f[i]为 days中第i日 到最后的旅行花费, 即i是days的索引
        状态转移: f[i] = min(f[days[j]]+costs[c]), j是旅行中的一天
        初始化: 空
        返回值: 0
        注意这个解法写成dp并不快, 因为i从后向前的过程中, j是从前向后, 会有重复
    解法3:
        解法1 bottom up
    解法4:
        解法2 bottom up
    解法5:
        空间换时间. 要想避免循环就要存很多数.
        用两个queue, 里边需要存(d, ans)的pair才行:
            dq7和dq30实质上重复, dq7是dq30的后半部分. 
        这个解法适用于 N很大, choice很少的情况
    解法6:
        用一个array和三指针, p当前位置, p7和p30的位置.
        这个解法适用于 choice多, N小的时候
        但其实也可以动态数组. 60的长度, 每当p到60就复制到0~30处
        但是这又变成了时间换空间了...
    """
    s = Solution()
    print(s.mincostTickets([1,4,6,7,8,20], [2, 7, 15]))
    print(s.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2, 7, 15]))
# @lc code=end

