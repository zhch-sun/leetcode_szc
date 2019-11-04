#
# @lc app=leetcode id=862 lang=python
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
from collections import deque
class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dq = deque()
        res = float('inf')
        N = len(A) 
        
        P = [0] * (N + 1)   # prefix sum, k为负数不好处理? 
        for i, n in enumerate(A):
            P[i + 1] = P[i] + n

        for i, n in enumerate(P):
            # 两个while顺序可以调换. 
            while dq and n - P[dq[0]] >= K:
                res = min(res, i - dq.popleft())  # Note 不能+1!!!
            while dq and n < P[dq[-1]]:
                dq.pop()
            dq.append(i) # 这里再append...
        return -1 if res == float('inf') else res

if __name__ == '__main__':
    """
    题设: 
        返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
        如果没有和至少为 K 的非空子数组，返回 -1
        1 <= A.length.  -10 ^ 5 <= A[i] <= 10 ^ 5
        K >= 1
    解法1:
        因为有负数, 双指针不行. 
        对值的二分可以: 
            cumsum之后, 维护最小值, 并与当前值比较, 只要一个满足即满足
    解法2: 单调队列
        求出prefix sum和之后P. 假设两个指针lo hi
        对于任意hi, 我们希望找到最小的lo. 使得P[hi]-P[lo]>=K
        精华: 
            如果lo1 < lo2, 但是P[lo2] < P[lo1], 则lo1不会是解
                所以只需要存储递增序列即可. 
            如果lo是解的一个可能, 则<=lo的值都不会构成未来的解. 因为
                这句话所以需要从头clean. 即需要queue. 
    """
    s = Solution()
    print(s.shortestSubarray([1], 1))     
    print(s.shortestSubarray([1,2], 4))     
    print(s.shortestSubarray([2,-1,2], 3))     
# @lc code=end

