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
    #     def helper(pos):  # TODO python 闭包应该用吗
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
        # python's 接近的解: 其实就是list comprehension
        mapping = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        pools = map(tuple, [mapping[int(i) - 2] for i in digits])
        result = [''] if digits else []
        for pool in pools:
            result = [x + y for x in result for y in pool] 
        return result
    
if __name__ == '__main__':
    """
    实际上是有bfs和dfs两种情况. 
    还是bfs最合理? dfs需要写一个recursion, 要么搞个stack..
    TODO dfs...
    """
    s = Solution()
    print(s.letterCombinations('23'))
        

