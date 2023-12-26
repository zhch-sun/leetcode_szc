#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#
import heapq
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(a, lo, hi, k):
            cur = a[lo]
            i, j = lo, hi + 1  #不能lo+1, hi,这样不支持区间只有一个元素
            while True:
                i += 1
                j -= 1                
                while i <= hi and a[i] < cur:
                    i += 1
                while j >= lo and a[j] > cur:
                    j -= 1
                if i >= j:
                    break  # 注意这里不是return
                a[i], a[j] = a[j], a[i]

            a[lo], a[j] = a[j], a[lo]
            return j
        
        def select(a, k):
            # 这意味着可以不需要递归, 直接while循环...            
            random.shuffle(nums)  # 容易忘
            k = len(nums) - k  # clever trick!!
            # k -= 1  # 如果不用上述trick, 需要-1 以及改正负!!!
            lo, hi = 0, len(nums) - 1
            while lo < hi:  # [lo, hi]一定有解
                j = partition(a, lo, hi, k)
                if j == k:
                    return a[j]
                elif j > k:
                    hi = j - 1
                else:
                    lo = j + 1
            return a[lo]  # 主循环有=这里也可以不写

        # return sorted(nums, reverse=True)[k-1]  # nums.sort()[k-1] 不行.. 95%
        # return heapq.nlargest(k, nums)[-1]  # 75%
        return select(nums, k)  # 62%

if __name__ == '__main__':
    """
    题设: 如题. 注意k一定是有效的且>=1, 所以也不用判断nums
    解法1: priority queue注意接口顺序
    解法2: quick selection
        quick selection主体是个二分!
        是第k大的数, 不是第k小的数... 容易忘. 
        可以 k = len(nums) - k. 或者改partition里面的小于号. 
        k-=1... 容易忘..
        记得要random
    """
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4], 2))
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 4))

