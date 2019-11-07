#
# @lc app=leetcode id=474 lang=python
#
# [474] Ones and Zeroes
#
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """        
        f = [[0] * (n + 1) for _ in xrange(m + 1)]  # Note 这里写反了.. 
        # for i in xrange(m + 1):  # Note 没有行列的初始化.....
        #     f[i][0] = 1
        for s in strs:
            num0 = s.count('0')
            num1 = s.count('1')
            for j in xrange(m, num0 - 1, -1):  # Note 01背包是反过来的!!!
                for k in xrange(n, num1 - 1, -1):  # Note 循环截止条件
                    f[j][k] = max(f[j][k], f[j-num0][k-num1] + 1) # 不需要if
        return f[-1][-1]

if __name__ == '__main__':
    """
    解法1:
        01背包二维cost问题: 
            把array里的str看成是物体. str的0和1的个数都是cost.
            最大化物体个数. 即这里0和1是二维的cost.
            特殊之处在于最大值是个数, 而01背包有个额外的优化目标.
        状态: 
            f[i][j][k] = v 前i个字符串, j是已经用的0的个数, 
                           k是已经用的1的个数, v是最大字符串个数
            f[i][j][k] = max(f[i-1][j][k], f[i-1][j-c1][k-c2]+1)
            f[i][j] = max(f[j][k], f[j-c1][k-c2]+1)
        初始化: 已经有+1了.. 全部0初始化
        返回值: f[-1][-1]
    解法2:
        震惊了, 居然有o(NlogN)的做法!!!!! 不考虑sort是O(N)!!!
        学术界貌似有不用sort的O(N)
        Linear Time Algorithms for Knapsack Problems with Bounded Weights
    解法3:
        dfs超时了..
    """
    s = Solution()
    print(s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
    print(s.findMaxForm(["10", "0", "1"], 1, 1))
    print(s.findMaxForm(["10","0001","111001","1","0"], 3, 4))  # 3
    print(s.findMaxForm(["0","11","1000","01","0","101","1","1","1","0",\
        "0","0","0","1","0","0110101","0","11","01","00","01111","0011",\
            "1","1000","0","11101","1","0","10","0111"], 9, 80))

