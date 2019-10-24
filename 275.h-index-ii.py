#
# @lc app=leetcode id=275 lang=python
#
# [275] H-Index II
#

# @lc code=start
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        N = len(citations)
        lo, hi = 0, N  # 应该理解成篇数, 或者h
        while lo < hi:  # lo==hi跳出循环
            mid = lo + (hi - lo + 1) // 2
            # if mid > 0 and citations[N - mid] >= mid:  # mid其实取不到0
            if citations[N - mid] >= mid:  # mid取不到0
                lo = mid
            else:
                hi = mid - 1
        return lo

if __name__ == '__main__':
    """
    题设: 
        h指数是指 他的的（N篇论文中）至多有h篇论文分别被引用了至少h次。
        给定的是排好序的数列
    解法1:
        继续循环不变量来理解. 
        解在[0, N], 所以lo hi是篇数而不是idx. 或者理解成h. 
        因为二分的时候mid都在中间, 而我的除法又是ceiling, 所以不需要mid>0的判断
    解法2:
        还是[lo, hi+1]更好一些. 但是不太好理解.. 又一个python答案
        citations[N-mid], 但是无法处理mid==0的情况? 
        但是不理解citations[mid]
        不写了. 
    """
    s = Solution()
    # print(s.hIndex([0 ))
    print(s.hIndex([1]))
    print(s.hIndex([0,1,3,5,6]))
# @lc code=end

