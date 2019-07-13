#
# @lc app=leetcode id=216 lang=python
#
# [216] Combination Sum III
#
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candi = list(xrange(1, 10))    
        res = []
        tmp = []
        self.backtrack(candi, n, tmp, 0, res, k)
        return res
    
    def backtrack(self, candi, target, tmp, left, res, k):
        if len(tmp) <= k:
            if target == 0 and len(tmp) == k:
                res.append(tmp[:])
            elif target > 0:
                for i in range(left, len(candi)):
                    item = candi[i]
                    tmp.append(item)
                    self.backtrack(candi, target-item, tmp, i + 1, res, k)
                    tmp.pop()

if __name__ == '__main__':
    """
    backtrack的内部的逻辑可以合并
    """
    s = Solution()
    print(s.combinationSum3(3, 9))
