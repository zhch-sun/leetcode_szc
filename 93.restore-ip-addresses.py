#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            if len(s) > 3 or len(s) == 0 or int(s) > 255 or (s[0] == '0' and len(s) > 1): # 注意括号里
                return False
            return True
                
        if len(s) < 4:
            return []
        res = []
        for i in range(1, 4):
            for j in range(i + 1, min(i + 1 + 3, len(s) - 1)): #注意边界条件
                for k in range(j + 1, min(j + 1 + 3, len(s))): #注意边界条件
                    if isValid(s[:i]) and isValid(s[i:j]) and isValid(s[j:k]) and isValid(s[k:]):
                        res.append(s[:i] + '.' + s[i:j] + '.' + s[j:k] + '.' + s[k:])
        return res

        
if __name__ == '__main__':
    """
    题设: 给一个数字字符串, 判断能够构成几个合法ip
    解法:
        也可以backtracking. 但还是直接写for循环. 
        [0, i] [i, j] [j, k] [k, len]
        TODO 倒序写应该更快? [k, len]应该经常不满足?
    """
    s = Solution()
    # print(s.restoreIpAddresses("25525511135"))
    # print(s.restoreIpAddresses("2012002123"))
    print(s.restoreIpAddresses("0000"))
