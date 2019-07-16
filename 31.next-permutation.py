#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cur = len(nums) - 1
        while cur >= 1 and nums[cur] <= nums[cur-1]:  # Note <=
            cur -= 1
        if cur == 0:
            nums.reverse()  # in place reverse
            return  # return nums
        prev = cur - 1
        next = cur
        while next + 1 < len(nums) and nums[next+1] > nums[prev]:
            next += 1
        nums[prev], nums[next] = nums[next], nums[prev]
        self.reverse(nums, prev+1, len(nums) - 1)
        return  # return nums

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
if __name__ == '__main__':
    """
    按照顺序的所有permutation，给出下一个
    https://blog.csdn.net/nomasp/article/details/49913627
    这个题的解法也可以搞46题47题。
    这个题实际上是要输出DFS搜索时的下一个位置。见最高回答的cdai评论。
    1. 第一步循环，从后向前，如果是1234立即停，如果是4321就走到0位置。
    因为第一个递增位置就是可以交换的位置。 34可以直接reverse就输出结果。
    2. 第二步循环，找到比当前上升节点大的最小值，交换一下：1243->1324
    3. 第三步reverse. 因为之前的大小关系，swap之后，后面的整个部分仍然是降序，
    所以可以直接reverse它们，变成升序。
    
    理解之后发现就是描述了实际发生的过程。。12345直接reverse最后两位，如果
    35421就找到第一个升序，然后交换，剩下的都变升序。
    python 没有inplace的reverse。。
    """
    s = Solution()
    print(s.nextPermutation([1,2,3,4]))
    print(s.nextPermutation([1,2,4,3]))
    print(s.nextPermutation([4,3,2,1]))
