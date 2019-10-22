#
# @lc app=leetcode id=77 lang=python
#
# [77] Combinations
#
class Solution(object):
    # def combine(self, n, k):
    #     """
    #     :type n: int
    #     :type k: int
    #     :rtype: List[List[int]]
    #     """
    #     res = [[]]  # 这个初始化. 
    #     for _ in range(k):
    #         res_new = []
    #         for item in res:
    #             start = item[-1] + 1 if item else 1  # 注意不是else 2!!
    #             for i in range(start, n + 1):
    #                 res_new.append(item + [i])
    #         res = res_new
    #     return res

    def combine(self, n, k):
        def dfs(n, k, tmp, res):
            if k == 0:
                res.append(tmp[:])  # 又忘了[:]..
                return 
            start = tmp[-1] + 1 if tmp else 1  # start是新的数所以+1
            for i in range(start, n + 1):  #  n + 1
                tmp.append(i)
                dfs(n, k - 1, tmp, res)
                tmp.pop()
        res = []
        dfs(n, k, [], res)
        return res

if __name__ == '__main__':
    """
    题设: 给定n, k, 生成所有组合; k隐含得必须小于等于n
    解法1: 
        循环, 第一次放所有数, 第二次放比前面都大的
        答案是在前面加的 [i] + item, 这样理论效率应该更低? 但是实际更快? 
    解法2:
        这种生成所有的题, backtrack是标准答案呀, 而且比循环快?
    解法3:
        还有个非backtrack的recursive答案. 就不搞了.
    """
    s = Solution()
    print(s.combine(4, 2))
