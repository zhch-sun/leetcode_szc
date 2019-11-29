#
# @lc app=leetcode id=47 lang=python
#
# [47] Permutations II
#
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """        
        def dfs(tmp):
            if len(tmp) == N:
                ans.append(tmp[:])  # Note 又忘了..
                return
            for i in xrange(N):  # 对nums循环
                # # 如果和上一个数字相同且同一个循环, 那么这个位置不再考虑
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue  # Note 用used[-1]除重!
                if not used[i]:
                    tmp.append(nums[i])
                    used[i] = True
                    dfs(tmp)
                    tmp.pop()
                    used[i] = False
            return

        N = len(nums)  # 不需要判断空
        nums.sort()
        used = [False] * N  # state for used
        ans = []
        dfs([])  # 也可nums转换成set, 这样就没有顺序了.
        return ans        

    # def permuteUnique(self, nums):
    #     def dfs(tmp, u, start):
    #         if u == N:
    #             ans.append(tmp[:])
    #             return
    #         for i in xrange(start, N):  # i是path的idx, u是nums的idx
    #             if not used[i]:
    #                 used[i] = True  # used表示tmp对应位置上是否有数
    #                 tmp[i] = nums[u]
    #                 # 这里的写法很神奇啊, 不用搞个循环. 只考虑下一个就好了.
    #                 n_start = i + 1 if u + 1 < N and nums[u+1]==nums[u] else 0
    #                 dfs(tmp, u + 1, n_start)
    #                 tmp[i] = None
    #                 used[i] = False
    #         return

    #     N = len(nums)
    #     nums.sort()
    #     tmp = [None] * N
    #     used = [False] * N
    #     ans = []
    #     dfs(tmp, 0, 0)
    #     return ans

    # def permuteUnique(self, nums):
    #     res = [[]]
    #     for i in xrange(len(nums)):
    #         num = nums[i]
    #         new_res = []
    #         for l in res:
    #             for i in xrange(len(l) + 1):
    #                 new_res.append(l[:i] + [num] + l[i:])
    #                 if i < len(l) and num == l[i]:  # 要先插入再判断
    #                     break
    #         res = new_res
    #     return res

if __name__ == '__main__':
    """
    分析: 
        认为相同的三个1, 分别是11, 12, 13, 且要求相同数字的相对顺序不变. 
    解法1:
        枚举每个位置放哪个数. 
        关键在于过滤方式, 不仅要nums[i] == nums[i - 1], 
        还要确保used[i-1] == False, 
        因为True的时候在递归的内环, False的时候才是同一个循环.
    解法2:
        枚举的是每个数字的位置. 
        需要数字的位置u, 数字枚举开始的位置start
    解法3:
        插入法不管了.
        To handle duplication, 
        just avoid inserting a number AFTER any of its duplicates.
    解法4:
        最快的解法居然是基于next_permu的写法. 也没有快很多.
    """
    s = Solution()
    print(s.permuteUnique([1,1,2]))
