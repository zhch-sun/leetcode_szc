#
# @lc app=leetcode id=504 lang=python
#
# [504] Base 7
#

# @lc code=start
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:  # 忘记了..
            return '0'
        isNeg = num < 0  # 优雅处理负数!
        num = abs(num)
        ans = []
        while num:
            num, val = divmod(num, 7)
            ans.append(str(val))
        if isNeg:
            ans.append('-')
        return ''.join(reversed(ans))  # Note倒序!

if __name__ == '__main__':
    """
    题设: 10进制->7进制, 
    坑:
        优雅处理负数, 
        进制转换要倒序! 
        处理0!
    """
    s = Solution()
    print(s.convertToBase7(100))
    print(s.convertToBase7(-7))
        
# @lc code=end

