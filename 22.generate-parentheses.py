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
        def dfs(tmp, nl, nr):
            if not nl and not nr:
                ans.append(tmp)
                return  # Note 又忘记了..
            # 左分支
            if nl > 0:  # Note 忘记了...
                nl -= 1
                dfs(tmp + '(', nl, nr)
                nl += 1
            # 右分支
            if nr > nl:
                nr -= 1  # 这里不能tmp += ')', 因为删不掉...
                dfs(tmp + ')', nl, nr)

        ans = []
        dfs('', n, n)
        return ans

    # def generateParenthesis(self, n):
    #     def dfs(n):
    #         if n == 0:
    #             return ans[0]
    #         if ans[n]:
    #             return ans[n]
    #         for i in xrange(n):
    #             left = dfs(i)
    #             right = dfs(n - i - 1)  # 笛卡尔积
    #             ans[n] += ['(' + l + ')' + r for l in left for r in right]
    #         return ans[n]

    #     ans = [[] for _ in xrange(n + 1)]
    #     ans[0] = ['']
    #     dfs(n)
    #     return ans[n]


if __name__ == '__main__':
    """
    题目：已知括号的对数, 给出所有可能的括号组合方案
    解法1:
        回溯. dfs. 按需剪枝. 即保证右边括号数大于左括号.
        复杂度分析很困难.
    解法2:
        官方解法3. DP
        https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode/
        第N中情况由第N-1种组合而来. 就是加括号的位置不同. 
        (left)+right: 枚举left right的情况(笛卡尔积), 就可以得到解. 
        证明包含所有情况: 枚举了新增()的所有位置. 
        证明没有冗余: 
            同样的分割: first内部互不相同, 加括号还是不一样. right不相同, 各不相同.
            不同的分割(n=4):
                左边0个右边三个 -> 左1右3
                左边1个右边两个 -> 左2右2  # 且不存在最左边的()的括号, 不会和上面重复
                左边两个右边1个 -> 左3右1
                左边三个右边0个 -> 左4右0
    """
    s = Solution()
    print(s.generateParenthesis(3))

