#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """        
        def dfs(tmp, idx, target):
            if target == 0:
                ans.append(tmp[:])
                return
            for i in xrange(idx, N):
                if target - nums[i] < 0:
                    break
                tmp.append(nums[i])
                dfs(tmp, i, target - nums[i])  # Note 这里是i!
                tmp.pop()
            return

        N = len(nums)
        nums.sort()  # 也可以reverse, 然后循环中continue
        ans = []
        dfs([], 0, target)
        return ans

    # def combinationSum(self, candidates, target):
    #     f = [[] for _ in xrange(target + 1)]
    #     f[0] = [[]]  # Note: 震惊! 初始化! 理解这个初始化含义!
    #     for n in candidates:
    #         for j in xrange(n, target + 1):
    #             f[j] += [tmp + [n] for tmp in f[j-n]]
    #     return f[-1]

if __name__ == '__main__':
    """
    题设: 
        给定一个无重复元素的数组和一个目标数，均为正整数. 
        无限选数, 返回使数字和为target的所有组合. list of list
        同类题目: 39 40 216 377
    解法: 
        dfs + backtrack. 
        和N-sum的区别在于，这个不限制N的个数。因此也只能用dfs穷举
        除重的方法是 递归dfs时用的是i而不是idx!!!
        复杂度:
            O(len(nums)^(target/min(nums)))
    解法2: DP, 
        完全背包, 但是返回的是具体的方案! 需要修改状态的定义. 
        空间复杂度比dfs还是变大很多. 
    """
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))
    print(s.combinationSum([2,3,5], 8))
