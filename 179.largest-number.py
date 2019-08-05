#
# @lc app=leetcode id=179 lang=python
#
# [179] Largest Number
#
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 100%!
        strs = map(str, nums)
        strs.sort(cmp=lambda x, y: [-1, 1][x + y < y + x])
        return '0' if strs[0]=='0' else ''.join(strs)

        
if __name__ == '__main__':
    """
    可以用这道题实现一下各种sort. mergesort quicksort insertsort. 
    没有公司考.. 估计是因为怎么证明呢? 
    s1 > s2 则 s2 < s1; s1 < s2, s2 < s3, 则 s1 < s3
    注意还有corner case: 多个0的输入..
    """
    s = Solution()
    print(s.largestNumber([10, 2]))
    print(s.largestNumber([3,30,34,5,9]))
    print(s.largestNumber([0, 0]))

