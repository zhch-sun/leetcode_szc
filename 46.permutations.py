#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
import itertools
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return itertools.permutations
        
if __name__ == '__main__':
    """
    TODO backtracking是什么鬼？？？
    确实是个dfs，只不过这里不是binary而是n-ary tree。
    dfs可以用swap，好处是省掉了memcopy的时间。python的答案都有很多memcopy
    还有iterative的做法，基础是插入法, 一个一个数字插入. 1只有一个位置, 2有两个, 3有 2*3=6个 4有6*4=64个
    https://leetcode.com/problems/permutations/discuss/18237/My-AC-simple-iterative-javapython-solution
    上面的做法要求copy array, 很慢. 下面用swap解决了这个问题. 生长过程是9*8*7*6*5... 不知道怎么证明, 不搞. 
    https://leetcode.com/problems/permutations/discuss/18378/Simple-python-code-without-recursion
    """
    s = Solution()
    

