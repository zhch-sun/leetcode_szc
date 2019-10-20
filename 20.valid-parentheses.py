#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for ch in s:
            if ch in mapping:
                if not stack or not stack.pop() == mapping[ch]:  # pop之前必须check是否为空
                    return False
            else:
                stack.append(ch)
        return not stack

if __name__ == '__main__':
    """
    two pitfalls
    1. the empty stack for popping
    2. in the end stack might not be empty
    """
    s = Solution()
    print(s.isValid('(()))'))

