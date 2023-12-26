#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#
class Solution(object):
    # def restoreIpAddresses(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[str]
    #     """
    #     def isValid(s):
    #         if len(s) > 3 or len(s) == 0 or int(s) > 255 or \
    #             (s[0] == '0' and len(s) > 1): # 注意括号里
    #             return False
    #         return True
        
    #     N = len(s)
    #     if N < 4 or N > 12:
    #         return []
    #     res = []
    #     for i in range(1, 4):
    #         for j in range(i + 1, min(i + 1 + 3, N - 1)): #注意边界条件
    #             for k in range(j + 1, min(j + 1 + 3, N)): #注意边界条件
    #                 if isValid(s[:i]) and isValid(s[i:j]) and isValid(s[j:k]) and isValid(s[k:]):
    #                     res.append(s[:i] + '.' + s[i:j] + '.' + s[j:k] + '.' + s[k:])
    #     return res

    def restoreIpAddresses(self, s):
        def isValid(s):
            if len(s) == 0 or len(s) > 3 or int(s) > 255 or \
                s[0] == '0' and len(s) > 1:  # Note 首位不能为0
                return False
            return True
        
        def dfs(tmp, idx, pos):
            if idx == 3:
                if isValid(s[pos:]):  # szc 我这样写还是很快哈哈
                    tmp.append(s[pos:])
                    ans.append('.'.join(tmp))
                    tmp.pop()  # Note 这里要pop...
                return
            for j in xrange(pos, min(pos + 3, N - (3 - idx))):  # 剪枝
                cur = s[pos: j + 1]
                if isValid(cur):
                    tmp.append(str(cur))
                    dfs(tmp, idx + 1, j + 1)
                    tmp.pop()
                else:
                    break  # 确实都可以跳出...
            return

        N = len(s)
        if N > 12 or N < 4:
            return []
        ans = []
        dfs([], 0, 0)  # idx
        return ans

if __name__ == '__main__':
    """
    题设: 给一个数字字符串, 判断能够构成几个合法ip
    解法1:
        dfs更快. 
        注意首位不能为0!
        快速原因:
            因为在第一个部分就可以early stoppping.
            最后一个part不循环! 直接到最后
            只要不valid就可以break! 加速显著. 
        甚至不需要迭代解法中的pruning
    解法1:
        for循环在最内环才判断. 所以慢
        [0, i] [i, j] [j, k] [k, len]
    """
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))
    print(s.restoreIpAddresses("2012002123"))
    print(s.restoreIpAddresses("0000"))
