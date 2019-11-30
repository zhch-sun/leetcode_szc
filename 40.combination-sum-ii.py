#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#
class Solution(object):
    def combinationSum2(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """        
        def dfs(tmp, idx, target):
            if target == 0:  # target == 0..
                ans.append(tmp[:])
                return 
            for i in xrange(idx, N):
                if nums[i] > target:
                    break
                # Note不是 i > 0
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                tmp.append(nums[i])
                dfs(tmp, i + 1, target - nums[i])
                tmp.pop()
            return

        ans = []
        N = len(nums)
        nums.sort()
        dfs([], 0, target)
        return ans

    # def combinationSum2(self, candidates, target):
    #     # 错解. 
    #     if sum(candidates) < target:
    #         return
    #     f = [[] for _ in xrange(target + 1)]
    #     f[0] = [[]]
    #     for n in candidates:
    #         for j in xrange(target, n - 1, -1):
    #             f[j] += [tmp + [n] for tmp in f[j - n]]
    #     return f[-1]

if __name__ == '__main__':
    """
    题设: 
        给定一个数组(可有重复)和一个目标数，每个数用一次.
        找出数组中所有可以使数字和为target的组合。 
    解法1: 
        简单理解: 111. 给每个1一个标号, 11, 12, 13, 
        他们之间的相互顺序不能变, 而且如果有12则11必须存在.
        所以在同一层循环中, 过滤和前一个相同的数. 
        复杂度: 
            时间O(2^n) 空间O(n) 
            在循环中, 每个数字都有两种可能, 选或者不选. 所以2^n.
            或者C(n,0) + c(n,1) + .. + c(n, n) = 2^n 
    解法2:
        是多重背包...
        这题不是01背包. 对于[10,1,2,7,6,1,5], 8. 
        1, 7 和 7 1是需要被过滤的, 而01背包过滤不了. 
        所以这题是多重背包.. 需要优先队列优化..
    """
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    print(s.combinationSum2([2,5,2,1,2], 5))
    print(s.combinationSum2([1,1,1,1,1,1], 2))
