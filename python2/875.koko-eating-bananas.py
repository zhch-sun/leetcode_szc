#
# @lc app=leetcode id=875 lang=python
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """解法1
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def isValid(piles, H, target):
            total = 0
            for p in piles:
                total += (p - 1) // target + 1  # 忘记+1
            return True if total <= H else False

        lo, hi = 1, max(piles)  # [lo, hi]
        while lo < hi:  # 注意不能加=号.. 会死循环在hi上
            mid = lo + (hi - lo) // 2
            if isValid(piles, H, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """解法2"""
        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            
            cnt = 0
            for p in piles:
                cnt += (p + mid - 1) // mid
            
            if cnt > h:
                lo = mid + 1
            else:
                hi = mid
        return lo

if __name__ == '__main__':
    """
    分析: 
        看清输入范围: 大于一且都是有意义的整数. 
        解得范围: 因为堆的长度小于H, 所以一定有解. 解得最大值是max(piles)
        注意求得是最小值.. 以此判定if else里面的赋值语句
    坑: 
        仔细分析isValid函数, 记得+1...
    """
    s = Solution()
    print(s.minEatingSpeed([3,6,7,11], 8))    
# @lc code=end

