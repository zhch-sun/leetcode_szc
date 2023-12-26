#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        head = 0 
        tail = len(s) - 1
        
        while head < tail:
            h = s[head]
            t = s[tail]
            if not h.isalnum():
                head += 1
                continue
            if not t.isalnum():
                tail -= 1
                continue
            if s[head].lower() == s[tail].lower():
                head += 1
                tail -= 1
            else:
                return False
        return True

    # def isPalindrome(self, s):
    #     s = [i.lower() for i in s if i.isalnum()]
    #     return s == s[::-1]
 
            
if __name__ == '__main__':
    """
    题设: 判断是否为回文. 只考虑字母数字, 忽略大小写
    解法1: 
        双指针即可, 循环中判断. 
        python: s.isalnum()
    解法2: 
        也可以先过滤一遍, 且直接比较reverse的..
        先过滤应该要快, 但是用额外内存.
    """
    s = Solution()
    print(s.isPalindrome("race a car"))

