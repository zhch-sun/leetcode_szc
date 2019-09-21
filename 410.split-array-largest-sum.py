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
        def valid(i, nums, m):
            # sum <= i
            count = 1  # =0 后面 count>=m, =1 count>m
            total = 0
            for item in nums:
                total += item
                if total > i:
                    total = item  # 大于的情况要赋值, 不能赋0, 等于的情况不用管
                    count += 1  
                    if count > m:  # 这里的count是加上了新的split之后的个数
                        return False
            return True
        
        lo = max(nums)
        hi = sum(nums)
        while lo <= hi:  # [lo,hi] -> [lo, hi+1]  lo==hi+1
            i = lo + (hi - lo) // 2
            if valid(i, nums, m):
                hi = i - 1
            else:
                lo = i + 1
        return lo

        
if __name__ == '__main__':
    """
    解法1: 99.1%
        还是二分查找, lo是max(num). hi是sum(num);
        给定一个值i可以查找是否存在一个配置, 方法就是遇到>=的就开一个新的split. 
        check函数中只要count个数小于m就说明可以这样分
        注意valid初值赋值为1可以简化逻辑, 和初值为0两种情况.  
    解法2: TODO
        DP 
    """
    s = Solution()
    print(s.splitArray([7,2,5,10,8], 2))
    
