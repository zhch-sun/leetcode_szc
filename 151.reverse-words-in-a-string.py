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
                    # 必须这里加空格，只有找到一个word才能在前面加。
                    s[insert] = ' '  
                    insert += 1
                hi = lo
                while hi < len(s) and s[hi] != ' ': # 先平移过去
                    s[insert] = s[hi]  
                    hi += 1  # hi == ' '
                    insert += 1
                reverse(s, insert - (hi - lo), insert - 1)  #再调换 
                lo = hi + 1
            else:  # Note这里需要else。。否则lo+的就不对了。。
                lo += 1
        return ''.join(s[:insert])

    # def reverseWords(self, s):
    #     def reverse(s, lo, hi):
    #         while lo < hi:
    #             s[lo], s[hi] = s[hi], s[lo]
    #             lo += 1
    #             hi -= 1

    #     def clean1(s):
    #         # inplace clean space: 在word后面加空格
    #         lo = hi = 0
    #         while hi < len(s):
    #             while hi < len(s) and s[hi] == ' ':  # 初始化消除前面的空格
    #                 hi += 1            
    #             while hi < len(s) and s[hi] != ' ':  # 复制中间的. 
    #                 s[lo] = s[hi]
    #                 hi += 1
    #                 lo += 1
    #             while hi < len(s) and s[hi] == ' ':  # 消除word后面的空格
    #                 hi += 1
    #             if hi < len(s):  # 如果没有在最后, 则必然后面有word, 所以可以加空格.
    #                 s[lo] = ' '
    #                 lo += 1
    #         return lo

    #     def clean2(s):
    #         # clean spaces: 在word前面加空格
    #         lo = hi = 0
    #         while hi < len(s):
    #             while hi < len(s) and s[hi] == ' ':  # 初始化消除前面的空格
    #                 hi += 1     
    #             if hi < len(s) and lo != 0:  # 忘记了hi < len(s)
    #                 s[lo] = ' '
    #                 lo += 1
    #             while hi < len(s) and s[hi] != ' ':  # 复制中间的. 
    #                 s[lo] = s[hi]
    #                 hi += 1
    #                 lo += 1
    #         return lo

    #     if not s:
    #         return s
    #     # reverse whole string          
    #     s = list(s)  # convert it to list to make it mutable
    #     reverse(s, 0, len(s) - 1)

    #     # reverse each word
    #     lo = hi = 0
    #     while lo < len(s):  # 这里必须是lo不能是hi, 因为最后的 lo+=1
    #         if s[lo] != ' ':
    #             hi = lo
    #             while hi < len(s) and s[hi] != ' ':
    #                 hi += 1
    #             reverse(s, lo, hi - 1)
    #             lo = hi + 1
    #         else:
    #             lo += 1

    #     lo = clean2(s)
    #     return ''.join(s[:lo])

if __name__ == '__main__':
    """
    题设: 翻转字符串中的单词, 去除多余空格. 76th简单版
    解法1: 库函数. 
    解法2：
        先整个reverse，再维护三个指针，
        插入位置insert，当前单词的开始结尾lo hi;
        天哪真是太复杂了。。面试的时候还是写解法3吧。。还是要熟练。。
    解法3: 
        reverse whole string, and reverse each word, clean space
        注意clean space还需要去除中间的多余空格.. 不仅是两头的. 写起来并不简单。。
        四个while循环
        clean1的解法最稳定.. 不容易出bug..
        clean2注意加空格除了lo==0还要保证hi<len(s)
    """
    s = Solution()
    print(s.reverseWords("a good   example"))
    print(s.reverseWords("  hello world!  "))
    print(s.reverseWords("the sky is blue"))
    print(s.reverseWords("  the  sky    is blue  "))

