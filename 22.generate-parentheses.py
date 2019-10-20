#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        tmp = ''
        self.dfs(res, tmp, n, n, n)
        return res

    def dfs(self, res, tmp, n, left, right):
        if left == 0 and right == 0:
            res.append(tmp[:])
            return # forget that...
        if left > 0:
            # tmp += '('  # This is wrong!!
            # left -= 1
            self.dfs(res, tmp+'(', n, left-1, right)
        if right > 0 and left < right:
            # tmp += ')'
            # right -= 1
            self.dfs(res, tmp+')', n, left, right-1)

if __name__ == '__main__':
    """
    题目：给出所有可能的括号组合
    答案总体来说两种，一种backtracking，一种dp。（python答案第三种不管）
    实际上前一种是dfs，后一种是bfs。
    dfs更简单，列出所有可能性的时候，按需剪枝。python答案里用了yield。
    TODO 所以唯一错的情况就是右括号个数大于左括号？怎么证明呢？
    TODO 但是yield能省内存是因为迭代器可以只以来之前的内容？这里仍然要维护之前的依赖路径？
    bfs需要推导出一种递推公式：分成两部分，(first)+second. 但这样要记录之前所有的的n所有情况。
    可以证明包含所有情况，可是是怎么说明没有冗余？
    实际上就是binary tree的生长？
    另外还需要想如果只需要output种类个数时，该怎么办。
    TODO dp没写吗。。
    """
    s = Solution()
    print(s.generateParenthesis(3))

