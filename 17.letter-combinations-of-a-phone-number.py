#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#
class Solution(object):
    # def letterCombinations(self, digits):
    #     """
    #     :type digits: str
    #     :rtype: List[str]
    #     """
    #     # my plain solution
    #     res = [] if not digits else ['']
    #     mapping = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    #     for i in digits:
    #         res_tmp = []  # forget this
    #         for d in mapping[int(i) - 2]:
    #             for cur in res:
    #                 res_tmp.append(cur+d)
    #         res = res_tmp
    #     return res

    # def letterCombinations(self, digits):
    #     # list comprehension version
    #     mapping = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    #     res = [] if not digits else ['']
    #     for d in digits:
    #         res = [r + m for m in mapping[int(d)-2] for r in res]
    #     return res

    # def letterCombinations(self, digits):
    #     # 68%
    #     from collections import deque
    #     if not digits:
    #         return []
    #     mapping = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    #     queue = deque([''])
    #     for i in digits:
    #         for _ in range(len(queue)):
    #             prev = queue.popleft()
    #             for d in mapping[int(i) - 2]:
    #                 queue.append(prev + d)
    #     return list(queue)

    # def letterCombinations(self, digits):
    #     # recursion
    #     mapping = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    #     def helper(pos):
    #         if pos < 0:  # have to add this
    #             return []
    #         if pos == 0:
    #             return list(mapping[int(digits[pos]) - 2])
    #         prev = helper(pos - 1)
    #         additional = mapping[int(digits[pos]) - 2]
    #         res = []
    #         for cur in additional:
    #             for item in prev:
    #                 res.append(item + cur)
    #         return res
    #     prev = ['']
    #     return helper(len(digits) - 1)
        
    def letterCombinations(self, digits):
        # 其实就是把我的答案用更多的list comprehension写了
        mapping = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        pools = map(tuple, [mapping[int(i) - 2] for i in digits])
        result = [''] if digits else []  # TODO corner case，感觉不如直接在前面讨论？
        for pool in pools:
            result = [x + y for x in result for y in pool]  # 这个顺序也可以换一下
        return result
    
if __name__ == '__main__':
    """
    本质是写一个笛卡尔积，cartesian product TODO 查询python实现
    简单解法包括list compr都需要两份res的内存。deque只需要一份内存

    实际上是有bfs和dfs两种情况. TODO 需要搞dfs吗？recursion太慢了？
    还是bfs最合理? dfs需要写一个recursion, 要么搞个stack..
    TODO dfs...
    TODO 前缀树是组成一个word，这道题和前缀树没有关系？因为要穷举？
    """
    s = Solution()
    print(s.letterCombinations('23'))
        

