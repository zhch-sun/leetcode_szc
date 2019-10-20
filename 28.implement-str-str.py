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
    还有rooling hash的答案. 不管。
    python的haystack[:i]生成了一个copy, 所有的slice都生成copy!
    TODO KMP算法, 还有个更快的BM算法, 还有Sunday算法（其实还有更快的）
    TODO 经典算法视情况放弃。
    python的实现是BM变种，不需要extra space
    链接 https://blog.csdn.net/v_july_v/article/details/7041827
    链接 https://www.jianshu.com/p/2e6eb7386cd3
    """
    s = Solution()
    print(s.strStr('abc', 'bc'))

