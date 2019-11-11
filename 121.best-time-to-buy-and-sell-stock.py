#
# @lc app=leetcode id=121 lang=python
#
# [121] Best Time to Buy and Sell Stock
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        # 算法使得不需要处理空输入.
        ans = 0  # 其实是globalMin
        curMin = float('inf')
        for n in prices:
            curMin = min(curMin, n)
            ans = max(ans, n - curMin)
        return ans

if __name__ == '__main__':
    """
    题设: 最多有一次交易, 找到最大收益. 
    解法1:
        推导: 
            以i位置为结尾的最小值是nums[i] - prevMin
            再加入一个变量记录globalMin即可.
        就是53题最大连续子序列和的psum版.
        直接记录curMIn, 更新ans即可. 
        背过写法, 这个写法最简单可靠. 
    """
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([7,6,4,3,1]))
