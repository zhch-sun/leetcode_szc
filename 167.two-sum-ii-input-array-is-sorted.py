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
        lo, hi = 0, len(numbers) - 1
        while lo < hi:  # 这里也可以check item == target因为一定有解. 
            # might overflow? no it's number not index
            item = numbers[lo] + numbers[hi]  
            if item == target:
                return lo + 1, hi + 1
            elif item < target:
                lo += 1
            else:
                hi -= 1
        return False
        
if __name__ == '__main__':
    """
    题设: 已经升序, 假设只有一个解. 不能重复使用相同元素. 
    理解1: 
        每次比较两头之和与 target的大小. 然后给lo+1或者hi-1
        用循环不变量来解释双指针法. 
        仍然是O(n)的复杂度!
    理解2: 
        same with 240th, 在一张有序2d矩阵上找点. 
        这个可以把矩阵旋转, 就变成了一个二叉搜索树!! 所有节点左边的leaf 小于右边的leaf
    解法2: 
        binary search貌似是nlogn,一个for循环接着binary search..太丑了. 
    """
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
