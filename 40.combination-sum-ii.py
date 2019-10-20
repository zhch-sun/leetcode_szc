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
        def dfs(candidates, target, res, left, tmp):
            if target == 0:
                res.append(tmp[:])
            elif target > 0:
                for i in range(left, len(candidates)):
                    item = candidates[i]
                    if item > target:  # 加速显著
                        break
                    # 仍然需要过滤1123这种. 注意是i-left不是i!!!
                    if i - left > 0 and item == candidates[i-1]:
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
    注意过滤条件. 
    TODO 为什么这个过滤是正确的呢？？？？？？
    比如111123.在第一个1的时候已经算出了所有包含1的情况
    """
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))
    print(s.combinationSum2([2,5,2,1,2], 5))
