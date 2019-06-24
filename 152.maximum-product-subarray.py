#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#
class Solution(object):
 

    # def maxProduct(self, nums):
    #     """
    #     注意这样做abs_pos不是以当前位置结尾的最大值! 只是当前结尾的最大正值,如果存在.
    #     比如[2, -4]的时候, -4处两个值, 一个-8 -4, 我的算法只存-8, 然而-4才是最大值. 
    #     但是通过gloal max解决了这个问题...
    #     """
    #     if not nums:
    #         return 0

    #     global_max = nums[0]
    #     abs_pos = nums[0] if nums[0] >= 0 else None
    #     abs_neg = nums[0] if nums[0] < 0 else None

    #     for cur in nums[1:]:
    #         prev_pos = abs_pos
    #         prev_neg = abs_neg

    #         pos_list = []  # note not list()
    #         neg_list = []
 
    #         choices = [cur]
    #         if prev_pos is not None:  # 这里不能用if prev_pos, 因为0的时候会跳过..... 
    #             choices.append(prev_pos * cur)
    #         if prev_neg is not None:
    #             choices.append(prev_neg * cur)

    #         for item in choices:
    #             if item >= 0:
    #                 pos_list.append(item)
    #             else:
    #                 neg_list.append(item)

    #         abs_pos = max(pos_list) if pos_list else None
    #         abs_neg = min(neg_list) if neg_list else None

    #         global_max = max(abs_pos, abs_neg, global_max)
    #     return global_max

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        global_max = nums[0]
        cur_max = cur_min = nums[0]
        for cur in nums[1:]:
            tmp = cur_max  # Note 需要这个tmp来防止max被改写..
            cur_max = max(cur_max * cur, cur_min * cur, cur)  # 状态转移!
            cur_min = min(cur_min * cur, tmp * cur, cur)  # 状态转移!
            global_max = max(cur_max, global_max)

        return global_max

if __name__ == '__main__':
    """
    我的想法:
    1. 之前的pos_max, neg_max, 这不行!. 因为需要的不是最大的负数(-12 -6取-6), 而是绝对值最大的负数. 
    2. 用cur_max和之前绝对值最大的负数? 也不行? 因为生成新的绝对值最大负数需要的是之前绝对值最大的正数, 而cur_max可能为负
    3. 所以用abs_pos和abs_neg是写成功了的, 问题是需要各种是否存在的条件判断, 而且实际情况很复杂..
    答案:
    用了cur_max,和cur_min
    是因为1. 这俩max完全依赖于cur_min和max, min完全依赖于max和min 2.cur_max足够生成global max
    具体三种情况, cur_max, cur_min均为正, 均为负, 一正一副, 针对cur的正负情况, 总共六种, 都是对的...
    TODO 有分治法的答案?
    """
    s = Solution()
    print(s.maxProduct([-2,0,-1]))
    print(s.maxProduct([2,3,-2,4]))
    # print(s.maxProduct([-4, -3, -2]))
    # print(s.maxProduct([-1, -2, -9, -6]))
    # print(s.maxProduct([2, -5, -2, -4, 3]))
    # print(s.maxProduct([-2,3,-4]))
    # print(s.maxProduct([-4, -3,-2]))


