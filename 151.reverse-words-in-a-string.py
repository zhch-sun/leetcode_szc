#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#
class Solution(object):
    # def reverseWords(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     return ' '.join(s.split()[::-1])
        
    def reverseWords(self, s):
        def reverse(s, lo, hi):
            while lo < hi:
                s[lo], s[hi] = s[hi], s[lo]
                lo += 1
                hi -= 1

        def clean_space(s):
            i = j = 0
            while j < len(s) and s[j] == ' ':
                j += 1
            while j < len(s):
                if s[j] != ' ':
                    s[i] = s[j]
                    i += 1
                j += 1


            return s, lo, hi
        if not s:
            return s
        # clean space            
        s = list(s)  # convert it to list to make it mutable
        lo, hi = 0, len(s) - 1
        while lo <= hi:
            if s[lo] == ' ':
                lo += 1
            elif s[hi] == ' ':
                hi -= 1
            else:
                break
        if lo > hi:
            return ''
        # reverse whole string
        reverse(s, lo, hi)   
        # reverse each word
        start = lo
        for i in range(lo, hi + 1):
            char = s[i]
            if char == ' ' or i == hi:
                reverse(s, start, i - 1)  # Note it is i - 1...
                start = i + 1
            

        ret = ''.join([s[i] for i in range(lo, hi+1)])
        return ret


if __name__ == '__main__':
    """
    解法1: 库函数. 
    解法2:
        clean space, reverse whole string, and reverse each word.
        注意还需要去除中间的多余空格.. 不仅是两头的. 
    """
    s = Solution()
    print(s.reverseWords("the sky is blue"))
    print(s.reverseWords("  the  sky    is blue  "))

