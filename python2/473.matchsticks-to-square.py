#
# @lc app=leetcode id=473 lang=python
#
# [473] Matchsticks to Square
#

# @lc code=start
class Solution(object):
    # def makesquare(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     def dfs(pos):  # 第pos根木棒
    #         if pos == N:  # 不需要 and sum(target) == 0
    #             return True  # 只要能进行到这一步, 就一定是可以.
    #         for i in xrange(4):  # 第i条边
    #             if target[i] >= nums[pos]:  # 太厉害了. 不用判断0!
    #                 target[i] -= nums[pos]
    #                 if dfs(pos + 1):
    #                     return True
    #                 target[i] += nums[pos]
    #         return False  # 如果4条边都失败

    #     total = sum(nums)
    #     if len(nums) < 4 or total % 4 or max(nums) > total // 4:
    #         return False
    #     N = len(nums)
    #     target = [total // 4] * 4
    #     nums.sort(reverse=True)
    #     return dfs(0)

    def makesquare(self, nums):
        def dfs(pos):  # 第pos根木棒
            if pos == N:  # 不需要 and sum(target) == 0
                return True  # 只要能进行到这一步, 就一定是可以.
            used = set()
            n = nums[pos]  # 用n减少array access
            for i, sz in enumerate(target):
                if sz >= n and sz not in used:  # 用sz减少数组访问
                    target[i] -= n
                    if dfs(pos + 1):
                        return True
                    target[i] += n
                    used.add(sz)
            return False  # 如果4条边都失败

        total = sum(nums)
        if len(nums) < 4 or total % 4 or max(nums) > total // 4:
            return False
        N = len(nums)
        target = [total // 4] * 4
        nums.sort(reverse=True)
        return dfs(0)      

if __name__ == '__main__':
    """
    题设: 
        给定一堆木棒, 必须全部都用, 组成正方形四条边
        698题一样且有DP的答案.
    分析:
        https://en.wikipedia.org/wiki/Partition_problem
        NP-complete.
        应该像其他问题一样dp解决, 
    解法1:
        迭代木棒而不是正方形的边. 
            每个木棒有四个选择, dfs内迭代四种情况, 
            显然是有冗余: 第一个木棒不需要讨论四种情况.
    解法2:
        解决第一根木棒会去试四个位置的情况:
            记录之前试过的边长! 如果已经试过就不再试
            由1000ms -> 60ms
        减少array access
            60ms -> 40ms  (最快的12ms)
    解法3:
        TODO 依次拼4条边, 用used表示用过的木棒.
        快速的原因应该是上面的解法需要判断四条边的情况才能退出,
        而这个解法只要凑不出第一条边, 就会跳出. early stopping.
        代码见最快的submission, 698题最快的sub不快?
        大雪菜的优化: 
            1.从大到小, 从剪枝角度来看? 
            2每条边内从大到小 
            3.当前长度木棒失败, 跳过所有长度相同 
            4.如果当前失败, 且是当前边的第一个, 则直接减掉. 
            5.当前失败且是最后一条边, 直接减掉.
    解法4:
        DP很慢未写. 见698题答案.
    """
    s = Solution()
    print(s.makesquare([1,1,2,2,2]))
    print(s.makesquare([3,3,3,3,4]))
    
# @lc code=end

