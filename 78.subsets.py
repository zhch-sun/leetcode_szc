#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
class Solution(object):
    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """ 
    #     def dfs(tmp, i):
    #         if i == N:
    #             ans.append(tmp[:])
    #             return
    #         tmp.append(nums[i])
    #         dfs(tmp, i + 1)
    #         tmp.pop()
    #         dfs(tmp, i + 1)

    #     if not nums:
    #         return []
    #     N = len(nums)
    #     ans = []
    #     dfs([], 0)
    #     return ans

    def subsets(self, nums):
        # 迭代子集的长度
        subsets = [[]]
        for n in nums:
            subsets += [s + [n] for s in subsets]  # Note +=
        return subsets if nums else []

    # def subsets(self, nums):
    #     # 二进制.
    #     N = len(nums)
    #     subsets = []
    #     for mask in xrange(2 ** N):  # Note不需要-1
    #         tmp = []
    #         for i, n in enumerate(nums):
    #             if mask >> i & 1:
    #                 tmp.append(n)
    #         subsets.append(tmp)
    #     return subsets

if __name__ == '__main__':
    """
    题设:
        给定一堆独立数, 返回其幂集. power set. 即所有可能的情况, 包含[]
        90题 follow
    解法1:
        回溯, 枚举每个数, 不是字典序!
        有两种可能, 选或者不选. 直到最后一个数结束才append
    解法1.5:
        答案中还有其他回溯做法, 需要记录nums的位置, 不管了
    解法2: 
        枚举每个长度的答案, 是字典序!
        也是枚举每个数. 
        先处理空集, 再处理[] + 1, 此时是所有1的情况. 
        这个集合加上(这个集合后面接2), 就是所有[] 1 2的情况, 以此类推
    解法3: 
        二进制: 更加generalize. 
        三个数时, 000 001 010... 表示这些状态. 正好对应是否取集合中元素
        所以从0枚举到2^n-1. (i >> j) & 1
    解法4:
        只循环二级制为1的位置, 省一半的时间. 先不管. 
    """
    s = Solution()
    print(s.subsets([1,2,3]))
