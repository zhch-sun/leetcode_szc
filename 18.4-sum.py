#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#
class Solution(object):
    # def fourSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """
    #     # 98% 
    #     def nSum(nums, target, N, left, before, res):
    #         if N == 2:
    #             l = left
    #             r = len(nums) - 1
    #             while l < r:
    #                 cur = nums[l] + nums[r]
    #                 if cur == target:
    #                     res.append(before + [nums[l], nums[r]])
    #                     l += 1
    #                     r -= 1
    #                     while l < r and nums[l] == nums[l - 1]:
    #                         l += 1
    #                     while l < r and nums[r] == nums[r + 1]:
    #                         r -= 1
    #                 elif cur < target:
    #                     l += 1
    #                 else:
    #                     r -= 1
    #         else: # 返回条件不能直接写在下面
    #             for idx in xrange(left, len(nums) - N + 1):
    #                 item = nums[idx]
    #                 if idx > left and item == nums[idx - 1]:  # Note this!!
    #                     continue
    #                 # TODO 第一个条件直接是target《N*item？第二个条件应该直接写在最前面？还有target很小的情况
    #                 if target - item < item * (N - 1) or target > nums[-1] * N:
    #                     break
    #                 nSum(nums, target-item, N-1, idx+1, before+[item], res)

    #     res = []
    #     nums.sort()
    #     nSum(nums, target, 4, 0, [], res)
    #     return res

    def fourSum(self, nums, target):
        def nSum(tmp, n, idx, target):
            if n == 2:
                lo, hi = idx, N - 1
                while lo < hi:
                    total = nums[lo] + nums[hi]
                    if total < target:
                        lo += 1
                    elif total > target:
                        hi -= 1
                    else:
                        ans.append(tmp + [nums[lo], nums[hi]])
                        while lo + 1 <= hi and nums[lo + 1] == nums[lo]:
                            lo += 1
                        while hi - 1 >= lo and nums[hi - 1] == nums[hi]:
                            hi -= 1
                        lo += 1
                        hi -= 1
            else:
                for i in xrange(idx, N - n + 1):
                    if i > idx and nums[i] == nums[i - 1]:
                        continue
                    if target < n * nums[i] or target > nums[-1] * n:  # prune!
                        break
                    tmp.append(nums[i])
                    nSum(tmp, n - 1, i + 1, target - nums[i])  # Note i + 1!
                    tmp.pop()

        nums.sort()
        N = len(nums)
        ans = []
        nSum([], 4, 0, target)
        return ans

if __name__ == '__main__':
    """
    这道题也是要除重，但是flag出的很少
    解法1：
        写一个general的n sum. 就是外层for循环，内层2sum.
        注意剪枝: target < n * nums[i] or target > nums[-1] * n
    解法2:
        见submission, 最快的解法仍然是3个循环 + set除重.
    """
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
