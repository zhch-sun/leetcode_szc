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
    解法1: 
    理解1: 可以用循环不变量来解释two pointers法. 
    解一定在两头中间. 如果两头的和不够大, 就增加l到1, (0点和其他任何值的和都小于0)
    理解2: same with 240th, 在一张有序2d矩阵上找点. 
    这个可以把矩阵旋转, 就变成了一个二叉搜索树!! 所有节点左边的leaf 小于右边的leaf
    
    解法2: binary search貌似是nlogn,一个for循环接着binary search..太丑了. 
    """
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))
