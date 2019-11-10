#
# @lc app=leetcode id=233 lang=python
#
# [233] Number of Digit One
#

# @lc code=start
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(i, total, limit):
            if i == N:
                return total
            if (not limit) and f[i][total] != -1:  # limit会影响值!
                return f[i][total]
            ans = 0
            up_bound = nums[i] if limit else 9  # 不要写10..
            for digit in xrange(up_bound + 1):  # 同一+1 
                ans += dfs(i + 1, total + (digit == 1), \
                    limit & (digit == nums[i]))
            if not limit:  # limit会影响求得值, 不应缓存. 但是也没关系.
                f[i][total] = ans 
            return ans
        
        if n <= 0:
            return 0
        nums = map(int, list(str(n)))
        N = len(nums)
        f = [[-1] * 15 for _ in xrange(15)]
        return dfs(0, 0, True)

if __name__ == '__main__':
    """
    解法1:
        数位dp其实就是穷举, 按照从高位到低位的顺序.
        total存储前i位已经有多少个1, 遇到i到达N时, 即已经越界, 把total返回.
        主循环根据limit确定循环范围, 穷举第i位的可能性, 
        limit还要注意两个地方: 
            1. 遇到limit时不可调用dp的memo. 
            2. 遇到limit也不要存储dp的memo. (存储也不影响)
    解法2: 
        数学找规律, 不管. 
    """
    s = Solution()
    print(s.countDigitOne(13))
    print(s.countDigitOne(1))
    print(s.countDigitOne(20))
# @lc code=end

