#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """        
        def twoSum(i, target):
            lo, hi = i, N - 1  # [lo, hi]
            while lo < hi:
                total = nums[lo] + nums[hi]
                if total == target:
                    ans.append([-target, nums[lo], nums[hi]])
                    while lo + 1 <= hi and nums[lo + 1] == nums[lo]:
                        lo += 1  # 留在最后一个和lo相等的位置
                    while hi - 1 >= lo and nums[hi - 1] == nums[hi]:
                        hi -= 1
                    lo += 1  # 更新位置
                    hi -= 1
                elif total < target:
                    lo += 1  # 下面可以接一个while循环除重, 但更慢
                else:
                    hi -= 1
            return

        N = len(nums)
        nums.sort()
        ans = []
        for i, n in enumerate(nums):
            if n > 0:  # 已经排过序了, 加速. 0可以替换成任意（target+2）//3
                break
            if i > 0 and nums[i] == nums[i - 1]:  # 除重
                continue
            twoSum(i + 1, -n)
        return ans

    # def threeSum(self, nums):
    #     def twoSum(i, target):
    #         lo, hi = i, N - 1  # [lo, hi]
    #         while lo < hi:
    #             total = nums[lo] + nums[hi]
    #             if total == target:
    #                 ans.add((-target, nums[lo], nums[hi]))
    #                 lo += 1  # 更新位置
    #                 hi -= 1
    #             elif total < target:
    #                 lo += 1  # 下面可以接一个while循环除重, 但更慢
    #             else:
    #                 hi -= 1
    #         return
    #     N = len(nums)
    #     nums.sort()
    #     ans = set()
    #     for i, n in enumerate(nums):
    #         if n > 0:  # 已经排过序了, 加速. 0可以替换成任意（target+2）//3
    #             break
    #         twoSum(i + 1, -n)  # 这里不除重, 会慢很多
    #     return list(ans)

if __name__ == '__main__':
    """
    题设: target=0, 需要除重. 
    解法1:
        sort之后每个元素来, 剩下的两个元素就是一个sorted 2sum.
        167th是sorted2sum：用循环不变量证明: 里面可能有多组解
        问题是除重: 
            一个是2sum内的重复, 一个是2sum间的重复（只要去除同一个最小值的重复即可）
            或者也可以sort之后再把所有解放到set里. (必须sort)
    解法2:
        把解变成tuple, 放到set除重. 
        因为已经排序了, 所以解不需要再排序.
    解法3:
        见submission最快的答案.
        直接循环+解用set, list除重. 要点在于第一个数一定负数, 第三个数一定正数.
        这样写没有顺序, 所以作者把解变成了set.  20ms...
    """
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))

