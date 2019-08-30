#
# @lc app=leetcode id=274 lang=python
#
# [274] H-Index
#
class Solution(object):
    # def hIndex(self, citations):
    #     """
    #     :type citations: List[int]
    #     :rtype: int
    #     """
    #     # citations.sort()  # 需要从小到大
    #     # N = len(citations)
    #     # for i, cite in enumerate(citations):  # 右边都大于cite
    #     #     if cite >= N - i:  # N-i 就是h(i是1-based, N是0-based)
    #     #         return N - i
    #     # return 0  # 处理全都是0, 以及空输入...
        
    #     citations.sort(reverse=True)  # 还是从大
    #     count = 0
    #     for i, cite in enumerate(citations):
    #         if cite >= i + 1:  # Note >=; Note i + 1
    #             count += 1
    #         else:
    #             break
    #     return count

        def hIndex(self, citations):
            N = len(citations) + 1
            count = [0] * (N + 1)
            for cite in citations:
                if cite < N:
                    count[cite] += 1
                else:
                    count[N] += 1
            total = 0
            for i in reversed(range(len(count))):
                total += count[i]  # i是cite数
                if total >= i:
                    return  i
            return 0

if __name__ == '__main__':
    """
    解法1: 从大到小
        画一下是个递减函数与f(x)=x的交点, 从大到小最后一个 cite > i的就是h index
        需要手动初始化count!
    
    解法2: bucket sort从大到小
        最后还是要算total, 区别在于一次加多个, 所以需要 >= 号.

    解法2: 从小到大, 其实很复杂.
        可能有多个: 从小到大时, 输出N-i, 所以第一个遇到的就是答案. 
        循环时, N-i是可能的h, 当前cite只需要与其对比即可. 
        [0, i] c < cite, num=i
        [i, N] c > cite, num=N-i(h)

    还有不用extra memory的counting sort.... 不管了. 
    """
    s = Solution()
    print(s.hIndex([3,0,6,1,5]))
    print(s.hIndex([100]))
    print(s.hIndex([0]))

