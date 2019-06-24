#
# @lc app=leetcode id=28 lang=python
#
# [28] Implement strStr()
#
class Solution(object):
    # def strStr(self, haystack, needle):
    #     """
    #     :type haystack: str
    #     :type needle: str
    #     :rtype: int
    #     """
    #     return haystack.find(needle)

    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        for i in range(len(haystack)-len(needle) + 1):
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1

        
if __name__ == '__main__':
    """
    还有rooling hash的答案. 
    python的haystack[:i]生成了一个copy, 所有的slice都生成copy!
    正则表达式? 
    TODO 有个KMP算法做这个 还有个更快的BM算法, 现在最快的是Sunday算法
    链接 https://blog.csdn.net/v_july_v/article/details/7041827
    链接 https://www.jianshu.com/p/2e6eb7386cd3
    """
    s = Solution()
    print(s.strStr('abc', 'bc'))

