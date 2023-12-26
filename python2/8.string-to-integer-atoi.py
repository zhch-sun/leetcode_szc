#
# @lc app=leetcode id=8 lang=python
#
# [8] String to Integer (atoi)
#
class Solution(object):
    # def myAtoi(self, s):
    #     """
    #     :type s: s
    #     :rtype: int
    #     """
    #     sign = 1
    #     idx = 0
    #     # white space
    #     while idx < len(s):
    #         if s[idx] != ' ':
    #             break
    #         idx += 1
    #     if idx == len(s):
    #         return 0
    #     # sign
    #     if s[idx] == '+':
    #         idx += 1
    #     elif s[idx] == '-':
    #         sign = -1
    #         idx += 1
    #     # integer number
    #     num = 0
    #     while idx < len(s):
    #         char = s[idx]
    #         if char.isdigit():
    #             if sign == 1:
    #                 num = num * 10 + int(char)
    #             else:
    #                 num = num * 10 - int(char)
    #             idx += 1
    #             # 这里如果是c的int的话需要提到前面判断..因为c已经溢出了..
    #             # 而且判断条件非常复杂
    #             # 但是c也可以用long来存最后的结果. 
    #             if num > 2 ** 31 - 1:
    #                 num = 2 ** 31 - 1
    #                 break
    #             elif num < -2 ** 31:
    #                 num = -2 ** 31
    #                 break
    #         else:
    #             break
    #     return num

    def myAtoi(self, s):
        idx = 0
        sign = 1
        num = 0
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -1 * 2 ** 31  # TODO 理解负数的补码？
        # white space
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        if idx == len(s):
            return 0
        # sign
        if s[idx] == '+' or s[idx] == '-':  #其实应该考虑只有一个‘-’的情况
            sign = -1 if s[idx] == '-' else 1
            idx += 1
        # integer number
        while idx < len(s) and s[idx].isdigit():
            # num = num * 10 + int(s[idx]) * sign
            num = num * 10 + (ord(s[idx]) - ord('0')) * sign  # 最后乘以sign也可以？
            if num > INT_MAX:
                num = INT_MAX
                break
            elif num < INT_MIN:
                num = INT_MIN
                break           
            idx += 1
        return num

if __name__ == '__main__':
    """
    将字符串转化为Int，处理trailing空格和符号, 开始循环后碰到任意非数字则跳出，
    如果超出32位则直接赋最大最小值
    需要维护idx sign和 num三个变量。
    中途时刻注意idx是否有效。
    1. 第一种做法中需要时刻check idx是否>len(s)
    TODO 2.正则表达式？？
    """
    s = Solution()
    print(s.myAtoi('-42'))
    print(s.myAtoi('-91283472332'))
