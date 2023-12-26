#
# @lc app=leetcode id=71 lang=python
#
# [71] Simplify Path
#
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """        
        # 剩余四种情况 '' '.' '..' 和字母
        tmp = path.split('/') 
        stack = []
        for item in tmp:
            if item == '..':
                if stack:
                    stack.pop()  # 不需要continue
            elif item != '' and item != '.':
                stack.append(item)
        return '/' + '/'.join(stack)

if __name__ == '__main__':
    """
    解法1:
        split之后还有四种情况, '' '.' '..' 和字母
        需要分类讨论. 前两种直接跳过. 
        坑:
            root的..还是root.
            最后的返回值, 是 '/' + ...
    """
    s = Solution()
    print(s.simplifyPath("/a//b////c/d//././/.."))
    print(s.simplifyPath("/../"))

