#
# @lc app=leetcode id=786 lang=python
#
# [786] K-th Smallest Prime Fraction
#
class Solution(object):
    def kthSmallestPrimeFraction(self, nums, k):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        def count(nums, mid, N):
            cnt, j = 0, 0
            p, q = 0, nums[N - 1]  # 需要初始化成最小值, pq是值不是index            
            for i in xrange(N):
                while j < N and float(nums[i]) / nums[j] > mid:
                    j += 1
                cnt += N - j 
                if j < N and float(nums[i]) / nums[j] > float(p) / q:
                    p, q = nums[i], nums[j]
            return cnt, p, q
        
        N = len(nums)
        nums.sort()
        lo, hi = 0, 1  # max不能直接求, 可以直接1
        
        while lo <= hi:  #[lo, hi]
            mid = lo + float(hi - lo) / 2
            cnt, p, q = count(nums, mid, N)
            if cnt == k:
                return [p, q]
            elif cnt < k:
                lo = mid
            else:
                hi = mid

        
if __name__ == '__main__':
    """
    题设: 
        一个已排序好的表 A，其包含 1 和其他一些素数.  
        当列表中的每一个 p<q 时，我们可以构造一个分数 p/q 。
        以整数数组的形式返回第 k 个最小的分数
    注意:
        从来没出现过这台题, 不考.
    解法: 
        p, q不是全局变量: 每次重新更新... 需要初始化成最小值, 注意是 0, nums[N - 1]
        count需要不同方向的旋转矩阵, 注意if中哪个j<N的判断
        可以把除法改成乘法加速..
    """
    s = Solution()
    print(s.kthSmallestPrimeFraction([1,2,3,5], 3))
    print(s.kthSmallestPrimeFraction([1,7], 1))
