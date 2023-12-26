#
# @lc app=leetcode id=402 lang=python
#
# [402] Remove K Digits
#

# @lc code=start
class Solution(object):
    # def removeKdigits(self, num, k):
    #     """
    #     :type num: str
    #     :type k: int
    #     :rtype: str
    #     """
    #     # early stopping版, 实际不快. 
    #     nums = list(num)
    #     N = len(nums)
    #     stack = []
    #     idx = 0
    #     # 实际for训话更快
    #     while k and idx < N:  # 这里也可以不加k用for循环, +k理论更快
    #         item = nums[idx]
    #         while k and stack and item < stack[-1]:
    #             stack.pop()
    #             k -= 1
    #         stack.append(item)
    #         idx += 1
    #     stack += nums[idx:]
    #     ans = ''.join(stack[:-k or None]).lstrip('0') # Note!!!
    #     return ans or '0'

    def removeKdigits(self, num, k):
        # for循环版, 实际更快.
        nums = list(num)
        N = len(nums)
        stack = []
        for n in nums:
            while k and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        stack = ''.join(stack[:-k or None]).lstrip('0') # 注意除0!!!
        return  stack if stack else '0'

if __name__ == '__main__':
    """
    解法: 
        肯定是从左向右greedy, 怎么证明呢? 
        Note 注意这题存的是item 而不是idx!!
    最后返回值得处理:
        int('')是非法的. 
        直接stack[:-k]即可, 不需要N-k....
        https://stackoverflow.com/a/15627413
        当k=0的时候, out[:0]返回None, 但是out[:None]返回整个list
    坑: 
        太容易忘了.....
        去掉最前面的0: lstrip('0')!!!!!
    """
    s = Solution()
    print(s.removeKdigits("1432219", 3))
    print(s.removeKdigits("10200", 1))
    print(s.removeKdigits("10", 2))
        
# @lc code=end

