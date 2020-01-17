#
# @lc app=leetcode id=90 lang=python
#
# [90] Subsets II
#
from collections import Counter, defaultdict
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        cnt = Counter(nums)  # defaultdict快得多
        for n, repeat in cnt.items():
            tmp = []
            for i in xrange(1, repeat + 1):
                tmp += [s + [n] * i for s in subsets]
            subsets += tmp
        return subsets if nums else []

    # def subsetsWithDup(self, nums):
    #     res = []
    #     tmp = []
    #     nums.sort()  # 别忘了sort..
    #     self.backtrack(nums, res, tmp, 0)
    #     return res

    # def backtrack(self, nums, res, tmp, pos):
    #     res.append(tmp[:])
    #     for i in xrange(pos, len(nums)):
    #         if i > pos and nums[i] == nums[i-1]:
    #             continue
    #         tmp.append(nums[i])
    #         self.backtrack(nums, res, tmp, i + 1)
    #         tmp.pop()

if __name__ == '__main__':
    """
    题设: 78题第一个, 区别是给定整数允许重复
    思路: 在同一个循环中如果遇到重复则continue, TODO 证明?
    解法1:
        类似78题解法2. 
        统计每个数出现的次数. 最终选择个数是c1 * c2 * c3
        先统计个数, 再枚举每个数字出现的个数. 
        类似题目: 求一个数约数的个数!:
            先求出质因数, 再统计每个的个数, 再组合他们.
    解法2:
        不写, 直接for循环, 不用统计数目, 奇技淫巧.
        https://leetcode.com/problems/subsets-ii/discuss/30166/Simple-python-solution-without-extra-space.
    解法3:
        比较丑陋的dfs,
    """
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))
