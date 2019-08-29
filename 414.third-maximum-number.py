#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#
import heapq
import random
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            # return heapq.nlargest(3, nums)[-1]
            return self.quickSelect(nums, len(nums) - 3)

    def quickSelect(self, a, k):
        def partition(a, lo, hi):
            i, j = lo, hi + 1
            cur = a[lo]
            while True:
                i += 1
                j -= 1
                while i <= hi and a[i] < cur:
                    i += 1
                while j >= lo and a[j] > cur:
                    j -= 1
                if i >= j:
                    break
                a[i], a[j] = a[j], a[i]
            a[lo], a[j] = a[j], a[lo]
            return j
        
        a = list(a)
        random.shuffle(a)
        lo, hi = 0, len(a) - 1
        while True:
            j = partition(a, lo, hi)
            if j == k:
                return a[k]
            elif j > k:
                hi = j - 1
            else:
                lo = j + 1

if __name__ == '__main__':
    """
    这个题就是要distinct的number. 我的实现是需要O(N)的额外空间. 答案其实也要O(N)空间
    https://leetcode.com/problems/third-maximum-number/discuss/90190/Java-PriorityQueue-O(n)-%2B-O(1)
    另外可以用 红黑树等有序符号表 存储三个数, 然后for循环. 但是红黑树的查询和插入应该都是logK, 所以不快
    """
    s = Solution()
    print(s.thirdMax([3,2,1]))
    print(s.thirdMax([1,2]))
    print(s.thirdMax([2,2,3,1]))
        
