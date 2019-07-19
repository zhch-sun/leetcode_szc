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
        p = path.split('/')
        stack = []
        for item in p:
            if item == '..':  #不能是if item=='..' and stack....　
                if stack:
                    stack.pop()
            # 注意如何收束逻辑!!!
            # elif item == '.' or item == '':
            #     continue
            # else:
            #     stack.append(item)
            elif item != '.' and item != '':
                stack.append(item)
            
        return '/' + '/'.join(stack)

if __name__ == '__main__':
    """
    注意最后的返回值, 是 '/' + ...
    """
    s = Solution()
    print(s.simplifyPath("/a//b////c/d//././/.."))
    print(s.simplifyPath("/../"))

