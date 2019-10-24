#
# @lc app=leetcode id=40 lang=python
#
# [40] Combination Sum II
#
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, res, lo, tmp):
            if target == 0:
                res.append(tmp[:])
            elif target > 0:
                for i in range(lo, len(candidates)):
                    item = candidates[i]
                    if item > target:  # 加速显著
                        break
                    # 仍然需要过滤1123这种. 注意是i-left不是i!!!
                    if i - lo > 0 and item == candidates[i-1]:
                        continue
                    tmp.append(item)
                    dfs(candidates, target-item, res, i+1, tmp)
                    tmp.pop()
        res = []
        tmp = []
        candidates.sort()
        dfs(candidates, target, res, 0, tmp)
        return res

if __name__ == '__main__':
    """
    题设: 
        给定一个数组(可有重复)和一个目标数，
        找出数组中所有可以使数字和为target的组合。 
        数组中每个数字在每个组合中只能用一次.
    解法: 
        在同一层循环中, 过滤和前一个相同的数. 
        过滤正确性: (111123,3) 
        只考虑顶层循环, 第一个1已经可以包含了所有含1的情况. 
        所以顶层循环中要过滤所有其余的1.
        第二层循环时, 第二个1包含了所有和为3-1且含有1的情况. 
        所以都过滤即可. 
    复杂度: 
        时间O(2^n) 空间O(n) why??? 
        Time complexity is O(2^n). Space complexity O(n). 
        在循环中, 每个数字都有两种可能, 选或者不选. 所以2^n.
        或者C(n,0) + c(n,1) + .. + c(n, n) = 2^n 
    """
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    print(s.combinationSum2([2,5,2,1,2], 5))
    print(s.combinationSum2([1,1,1,1,1,1], 2))
