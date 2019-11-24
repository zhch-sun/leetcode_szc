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
        # 居然一遍ac...
        def reverse(nums, i, j):  # [i, j]
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1  # Note 别忘.
                j -= 1

        N = len(s)
        nums = list(s)  # Note 别忘
        reverse(nums, 0, N - 1)  # Note 别忘
        
        k = 0  # 下一个要插入的位置
        lo = 0
        while lo < N:
            while lo < N and nums[lo] == ' ':
                lo += 1
            if lo == N:  # 必须要这里, 考虑下面k的正确位置.
                break
            if k != 0:  # 必须在word前面加空格, 不知道后面有没有新word
                nums[k] = ' '
                k += 1
            hi = lo
            while hi < N and nums[hi] != ' ':
                hi += 1
            hi -= 1  # 上面跳出时, hi已经越界.
            reverse(nums, lo, hi)  # 交换
            for i in xrange(lo, hi + 1):  # 平移
                nums[k] = nums[i]
                k += 1
            lo = hi + 1
        return ''.join(nums[:k])

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
    分析: python inplace的reverse是不接受参数的. 
    解法1: 库函数. 
    解法2：标准写法. 
        先整个reverse，再维护三个指针，
        插入位置k，当前单词的开始结尾lo hi;
        顺序:
            1. 去除word前空格
            2. 判断到最后并跳出. 
            3. 否则在一个word开端, 加上word前空格.
            4. 找到word结尾, 翻转
            5. copy到k开始的位置..
        注意: 
            先转list 并reverse..
            插入空格的方法: 必须再新开始一个word的前面插入, 
                在word后插入需要很多条件判断
    解法3: 
        分开写. 
        先clean前后的空格, 再调转. 最后再clean word中间多出的空格
        四个while循环
        clean1的解法最稳定.. 不容易出bug..
        clean2注意加空格除了lo==0还要保证hi<len(s)
    """
    s = Solution()
    print(s.reverseWords("a good   example"))
    print(s.reverseWords("  hello world!  "))
    print(s.reverseWords("the sky is blue"))
    print(s.reverseWords("  the  sky    is blue  "))

