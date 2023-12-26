#
# @lc app=leetcode id=698 lang=python
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(pos):
            if pos == N:
                return True
            n = nums[pos]
            used = set()
            for i, sz in enumerate(target):
                if sz >= n and sz not in used:
                    target[i] -= n
                    if dfs(pos + 1):
                        return True
                    target[i] += n
                    used.add(sz)
            return False

        total = sum(nums)
        nums.sort(reverse=True)  # Note忘记reverse=True了....
        if len(nums) < k or total % k != 0 or nums[-1] > total // k:
            return False
        N = len(nums)
        target = [total // k] * k
        return dfs(0)

if __name__ == '__main__':
    """
    题设: 
        n个数分成k份, sum相等.
        473题是前置条件
    解法1:
        居然TLE了.... 因为sort没有reverse=True
        32ms, 80%
    """
    s = Solution()
    # print(s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))      
    print(s.canPartitionKSubsets([18,20,39,73,96,99,101,111,114,190,207,295,471,649,700,1037]
, 4))      
# @lc code=end

