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

        if not s:
            return s
        # reverse whole string          
        s = list(s)  # convert it to list to make it mutable
        reverse(s, 0, len(s) - 1)
        
        insert = 0 # points to the pos to be written
        lo = 0  # begin of current word, end of current word
        while lo < len(s):
            if s[lo] != ' ':
                if insert != 0:
                    s[insert] = ' '  # 必须这里加空格，只有找到一个word才能在前面加。
                    insert += 1
                hi = lo
                while hi < len(s) and s[hi] != ' ':  #必须调换顺序。。 先判断len。。
                    s[insert] = s[hi]
                    hi += 1  # hi == ' '
                    insert += 1
                reverse(s, insert - (hi - lo), insert - 1)
                lo = hi + 1
            else:  # Note这里需要else。。否则lo+的就不对了。。
                lo += 1
            # 因为corner case不能在这里加空格。

        return ''.join(s[:insert])


if __name__ == '__main__':
    """
    解法1: 库函数. 
    解法2：
        先整个reverse，再维护三个pointer，insert，beginword, endword
        天哪真是太复杂了。。面试的时候还是写解法3吧。。还是要熟练。。
    解法3: 
        clean space, reverse whole string, and reverse each word.
        注意clean space还需要去除中间的多余空格.. 不仅是两头的. 写起来并不简单。。
        四个while循环
    """
    s = Solution()
    print(s.reverseWords("a good   example"))
    print(s.reverseWords("the sky is blue"))
    print(s.reverseWords("  the  sky    is blue  "))

