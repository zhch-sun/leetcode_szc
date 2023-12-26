#
# @lc app=leetcode id=410 lang=python
#
# [410] Split Array Largest Sum
#
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def isValid(nums, target, m):
            count = 1  # =0 后面 count>=m, =1 count>m
            total = 0
            for item in nums:
                total += item
                if total > target:
                    total = item  # 大于的情况要赋值, 不能赋0, 等于的情况不用管
                    count += 1  
                    if count > m:  # 这里的count是加上了新的split之后的个数
                        return False
            return True
        
        lo = max(nums)
        hi = sum(nums)
        while lo < hi:  # 一定有解 [lo, hi]
            mid = lo + (hi - lo) // 2
            if isValid(nums, mid, m):
                hi = mid
            else:
                lo = mid + 1
        return lo
        
if __name__ == '__main__':
    """
    题设: 
        给定一个非负整数数组和一个整数 m, 将这个数组分成 m 个非空的连续子数组
        使得这 m 个子数组各自和的最大值最小, 返回这个和
        注意非负很重要. 
    解法1: 99.1% Nlog(sum(A)). 注意即使sum(A)正比与N方也不要紧..
        值的二分查找, lo是max(num). hi是sum(num);
        给定一个值i可以查找是否存在一个配置, 方法就是遇到>=的就开一个新的split. 
        isValid函数很重要:
            1. count初值为1是因为array最后总有一个部分是没算的. 
            2. 可以这样写是因为没有任何一个元素单独大于target.
            3. total在开始新part时的初值很灵性
            4. early stopping
    解法2: N2 * M
        i组, 到j位置, k<j
        f[i][j] = min(f[i][j], max(f[i-1][k], presum[j] - presum[k]))
    """
    s = Solution()
    print(s.splitArray([7,2,5,10,8], 2))
