#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:  # 这里也可以check item == target因为一定有解. 
            # might overflow? no it's number not index
            item = numbers[l] + numbers[r]  
            if item == target:
                return l + 1, r + 1
            elif item < target:
                l += 1
            else:
                r -= 1
        return False
        
if __name__ == '__main__':
    """
    same with 240th, 在一张有序2d矩阵上找点. 有帮助吗?
    这道题是个对称矩阵.
    貌似可以用循环不变量来解释two pointers法. 
    binary search貌似是nlogn,一个for循环接着binary search..太丑了. 
    """
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
