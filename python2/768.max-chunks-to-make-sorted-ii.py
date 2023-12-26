#
# @lc app=leetcode id=768 lang=python
#
# [768] Max Chunks To Make Sorted II
#

# @lc code=start
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        for item in arr:
            if stack and item < stack[-1]:
                maxV = stack.pop()
                while stack and item < stack[-1]:
                    stack.pop()
                stack.append(maxV)
            else:  # Note 必须有这个else!!!!
                stack.append(item) 
        return len(stack)

if __name__ == '__main__':
    """
    思路:
        应该是先 对值的二分: 不行
        再理解升序的时候每个值都是一个chunk, 降序的时候整体是一个chunk.
        所以每个chunk可以维护两个指针, 可以证明lo指针不重要
        所以就是单调栈. 
    解法: 
        每个chunk是个范围, 所有chunk单调递增.
        即下一个chunk的最小值大于上一个chunk的最大值
        
        即循环中出现任意一个值小于之前存储的最大值, 都要merge. 
        merge的时候要删除上一个chunk里大于它的数, 并保留max. 
        即我们用最大值作为块的代表. 
        
        不需要最小值的原因是, 单调栈本身满足后面一定大于前面. 
    参考: 
    https://leetcode.com/problems/max-chunks-to-make-sorted-ii/discuss/135830/c%2B%2B-Using-Stack-with-O(n)-space-and-time-complexity.-With-7-lines.-4ms.-Beats-100
    
    """
    s = Solution()
    # print(s.maxChunksToSorted([5,4,3,2,1]))     
    # print(s.maxChunksToSorted([2,1,3,4,4]))     
    print(s.maxChunksToSorted([4,2,2,1,1]))     
    print(s.maxChunksToSorted([1,1,0,0,1]))     
# @lc code=end

