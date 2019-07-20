#
# @lc app=leetcode id=89 lang=python
#
# [89] Gray Code
#
class Solution(object):
    # def grayCode(self, n):
    #     """
    #     :type n: int
    #     :rtype: List[int]
    #     """
    #     res = [0]
    #     for _ in range(n):
    #         sz = len(res)
    #         for i in range(sz):
    #             item = res[i]
    #             if i % 2 == 0:
    #                 res.append(item << 1)
    #                 res.append(item << 1 | 1)
    #             else:
    #                 res.append(item << 1 | 1)
    #                 res.append(item << 1)
    #         res = res[sz:]
    #     return res

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):  # 循环中不能改变res的值.. 
                res.append(res[j] | 1 << i)
        return res
        
if __name__ == '__main__':
    """
    解法1
    还是iterative的对称解法最合适? 可以由n=2生成n=3, 有对称性. 
    00,01,11,10 -> (000,001,011,010 ) (110,111,101,100)
    我的第一种解法是在00尾巴上加0和加1
    解法2
    但实际上也可以在头上加... 而且前四个不变(前面加0), 后面是头+1, 但是这个要倒序. 
    Note 这道题很容易写出死循环... 在循环中改变res的值...
    解法3
    有一个可以通过bit操作从上一个数字生成下一个的方法. 
    """
    s = Solution()
    print(s.grayCode(2))
