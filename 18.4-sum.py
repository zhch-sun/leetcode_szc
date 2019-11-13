#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 98% 
        def nSum(nums, target, N, left, before, res):
            if N == 2:
                l = left
                r = len(nums) - 1
                while l < r:
                    cur = nums[l] + nums[r]
                    if cur == target:
                        res.append(before + [nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif cur < target:
                        l += 1
                    else:
                        r -= 1
            else: # 返回条件不能直接写在下面
                for idx in xrange(left, len(nums) - N + 1):
                    item = nums[idx]
                    if idx > left and item == nums[idx - 1]:  # Note this!!
                        continue
                    # TODO 第一个条件直接是target《N*item？第二个条件应该直接写在最前面？还有target很小的情况
                    if target - item < item * (N - 1) or target > nums[-1] * N:
                        break
                    nSum(nums, target-item, N-1, idx+1, before+[item], res)

        res = []
        nums.sort()
        nSum(nums, target, 4, 0, [], res)
        return res


if __name__ == '__main__':
    """
    这道题也是要除重，但是flag出的很少
    两种做法：
    1. 写一个general的n sum. 就是外层for循环，内层2sum.
    2. 外面两个用dict记录，内层2sum. 但是有o(n2)的space呀.. 而且实际速度也不快? 不写了. 
    """
    s = Solution()
    # print(s.fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
