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
            count = [0] * (N + 1)  # Note N+1, 也就是0不用
            for cite in citations:
                if cite < N:
                    count[cite] += 1  # 1-indexed
                else:
                    count[N] += 1
            total = 0
            for i in reversed(range(len(count))):  # N+1从N到0
                total += count[i]  # i是cite数!!
                if total >= i:  # 这里total是1-indexed, i也是
                    return i  # 如果文章数大于等于引用, 返回i, 即小的那个
            return 0

if __name__ == '__main__':
    """
    题设: 
        h指数是指他（她）的（N篇论文中）至多有h篇论文分别被引用了至少h次。
        （其余的 N - h 篇论文每篇被引用次数不多于 h 次。）

    解法1:
        https://leetcode-cn.com/problems/h-index/solution/hzhi-shu-by-leetcode/ 
        x轴文章数量, y轴引用次数, 降序排列. 
        画一下是个递减直方图与f(x)=x的交点, 从大到小最后一个cite>i的就是解
        需要手动初始化count!
        从小到大很复杂, 不考虑!
            可能有多个?? 从小到大时, 输出N-i, 所以第一个遇到的就是答案. ?
            循环时, N-i是可能的h, 当前cite只需要与其对比即可. 
            [0, i] c < cite, num=i
            [i, N] c > cite, num=N-i(h)
    
    解法2: bucket sort, 然后再从大到小
        最后还是要算total, 区别在于一次加多个, 所以需要 >= 号.
        为什么是return i 而不是 i+1??????

    解法3: 
        一个O(1)space的quick select, 貌似是最快的
        https://leetcode.com/problems/h-index/discuss/70823/O(N)-time-O(1)space-solution
        https://leetcode.com/problems/h-index/discuss/70927/Better-solution-than-Hint-no-extra-space
    还有不用extra memory的counting sort.... 不管了. 
    """
    s = Solution()
    print(s.hIndex([3,0,6,1,5]))
    print(s.hIndex([100]))
    print(s.hIndex([0]))

