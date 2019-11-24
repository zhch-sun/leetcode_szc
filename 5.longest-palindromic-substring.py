#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#
class Solution(object):
    # def longestPalindrome(self, s):
    #     # DP解法, 循环sz
    #     N = len(s)  # 不需要判断s==''
    #     f = [[False] * N for _ in xrange(N)]
    #     ans = ''
    #     for sz in xrange(1, N + 1):  # Note 这里是N+1...
    #         for i in xrange(0, N - sz + 1):  # Note 这里+1
    #             j = i + sz - 1
    #             f[i][j] = s[i] == s[j] and (sz < 3 or f[i + 1][j - 1])
    #             if f[i][j] and sz > len(ans):
    #                 ans = s[i:j+1]  # 这里可以记录ij位置避免copy
    #     return ans

    # def longestPalindrome(self, s):
    #     # DP 循环i, j
    #     N = len(s)
    #     f = [[False] * N for _ in xrange(N)]
    #     ans = ''
    #     for j in xrange(N):  # 我喜欢的循环方式. 
    #         for i in xrange(j, -1, -1):  # 这题特殊, 这里正序也是正确的!
    #             sz = j - i + 1
    #             f[i][j] = s[i] == s[j] and (sz < 3 or f[i + 1][j - 1])
    #             if f[i][j] and sz > len(ans):
    #                 ans = s[i:j+1]
    #     return ans

    # def longestPalindrome(self, s):
    #     # DP 空间O(N)
    #     N = len(s)
    #     f = [False] * N
    #     ans = ''
    #     for j in xrange(N):
    #         for i in xrange(j + 1):  # 因为也可以正序, 所以空间可以O(N)
    #             sz = j - i + 1
    #             f[i] = s[i] == s[j] and (sz < 3 or f[i + 1])
    #             if f[i] and sz > len(ans):
    #                 ans = s[i:j+1]
    #     return ans

    # def longestPalindrome(self, s):
    #     # 中心扩散法
    #     def expand(i, j):
    #         while i >= 0 and j < N and s[i] == s[j]:
    #             i -=  1
    #             j += 1
    #         return j - i - 1  # 跳出时比实际大小+2
       
    #     N = len(s)
    #     ans = ''
    #     for i in xrange(N):
    #         sz = expand(i, i)  # Note: 奇偶两种情况!
    #         if sz > len(ans):
    #             rd = (sz - 1) // 2
    #             ans = s[i - rd: i + rd + 1] 
    #         sz = expand(i, i + 1)  # expand函数处理越界问题
    #         if sz > len(ans):
    #             rd = sz // 2 - 1
    #             ans = s[i - rd: i + rd + 2]
    #     return ans

    def longestPalindrome(self, s):
        # 中心扩散法
        def expand(i, j):
            # 一定会进入循环.
            while i >= 0 and j < N and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1  # [i, j]  # 跳出时两边都大了1
        
        ansl, ansr = 0, 0  # [ansl, ansr]
        N = len(s)
        for i in xrange(N - 1):
            l, r = expand(i, i)
            if r - l > ansr - ansl:  # 用全局变量的话可以放到expand里.
                ansr, ansl = r, l
            l, r = expand(i, i + 1)
            if r - l > ansr - ansl:
                ansr, ansl = r, l            
        return s[ansl: ansr + 1]

if __name__ == '__main__':
    """
    解法1: 
        DP 外层循环sz(不推荐, 还是循环i,j好)
        f[i][j]表示 区间i,j是否为回文子串. 
        f[i][j] = f[i + 1][j - 1] & (s[i] == s[j])
        因为问题的对称性质, 这题必须循环length, 而不能i,j
        Note 再主循环中考虑sz=1 sz=2时的判断条件.
        结果输出: 
            不是最后搞个for循环输出, 直接在主循环中判断赋值. 
            也可以存ij 避免copy str
    解法2: 
        DP 循环 i, j
    解法3: 
        优化空间
        1 1 1 0
        0 1 1 0
        0 0 1 0
        下面的矩阵, 每次是写右边一列. 只依赖于j-1列
        但还是因为这题特殊, 内环也可以正序, 所以才能优化到O(N)
    解法4:
        标准解法: 中心扩展法. 
        注意处理奇偶两种情况. 
    解法5: 
        马拉车manacher算法. 
        基于中心扩散, 用了kmp的思路, 空间换时间.
        1. 先填充#处理奇偶性.
        2. 用一个数组P保存s中每个位置的最大扩展半径.
        https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
        Manacher algorithm https://www.hackerearth.com/zh/practice/algorithms/string-algorithm/manachars-algorithm/tutorial/
        https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/Manacher-algorithm-in-Python-O(n)
    """
    s = Solution()
    print(s.longestPalindrome('a'))
    print(s.longestPalindrome('babad'))
    print(s.longestPalindrome('cbbd'))
    print(s.longestPalindrome('dakffdadff'))

