#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#
from itertools import product
from collections import deque

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """    
        # 基础解法
        mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        ans = ['']
        for d in digits:
            tmp = []
            for pre in ans:  # 先循环ans保证字典序
                for char in mapping[int(d)]:
                    tmp.append(pre + char)
            ans = tmp
        return ans if ans[0] else []  # corner case...
    
    # def letterCombinations(self, digits):
    #     # list comprehension 写法
    #     mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    #     ans = ['']
    #     for d in digits:
    #         ans = [pre + char for pre in ans for char in mapping[int(d)]]
    #     return ans if ans[0] else []  # corner case...    

    # def letterCombinations(self, digits):
    #     # dq写法
    #     mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    #     dq = deque([''])
    #     for d in digits:
    #         chars = mapping[int(d)]
    #         for _ in xrange(len(dq)):
    #             pre = dq.popleft()  # 只有这样才是字典序.
    #             for char in chars:
    #                 dq.append(pre + char)
    #     return list(dq)

    # def letterCombinations(self, digits):
    #     def dfs(tmp, digits):
    #         if len(digits) == 0:
    #             ans.append(tmp)
    #             return
    #         for char in mapping[int(digits[0])]:
    #             dfs(tmp + char, digits[1:])
        
    #     mapping = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    #     if not digits:
    #         return []
    #     ans = []
    #     dfs('', digits)
    #     return ans

if __name__ == '__main__':
    """
    分析:  
        本质是写一个笛卡尔积，cartesian product
        不能直接用python的itertools.product, 因为返回的是tuple!
        这道题是穷举, 和前缀树应该没关系.
    解法1:
        双重循环. 先pre再ans保证字典序. 
    解法2:
        list comprehension
    解法3:
        deque: 可以省内存. 
    解法4:
        dfs/ backtrack
    """
    s = Solution()
    print(s.letterCombinations('23'))
