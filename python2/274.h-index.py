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
    #     # 从大到小for循环写法
    #     citations.sort(reverse=True)  # 还是从大到小
    #     count = 0
    #     for i, cite in enumerate(citations):  # i永远取不到 N
    #         if cite >= i + 1:  # Note >=; Note i + 1
    #             count += 1
    #         else:
    #             break
    #     return count
    
    def hIndex(self, citations):
        # 从大到小while写法
        citations.sort(reverse=True)  # 还是从大到小
        i = 0
        while i < len(citations) and citations[i] >= i + 1:
            i += 1
        return i

    # def hIndex(self, citations):
    #     N = len(citations)
    #     count = [0] * (N + 1)  # Note N+1, 也就是0不用
    #     for cite in citations:
    #         count[min(cite, N)] += 1
    #     total = 0
    #     for cite in xrange(N, -1, -1):  # 从N到0循环, 取到0则不需要最后return 0
    #         total += count[cite]
    #         if total >= cite:  # 这里total是1-indexed, i也是
    #             return cite # 如果文章数大于等于引用, 返回cite, 即小的那个

if __name__ == '__main__':
    """
    题设: 
        h指数是指 他的的（N篇论文中）至多有h篇论文分别被引用了至少h次。
        （其余的 N - h 篇论文每篇被引用次数不多于 h 次。
    思路: 
        数学上的不动点. 官方solu: 
        https://leetcode-cn.com/problems/h-index/solution/hzhi-shu-by-leetcode/ 
        官方solu里的图的交线是对的! 要理解! 需要找到一个错误的位置然后倒推. 
        应该通过循环不变量直接用while loop.
        主要的坑是 [] [0] [1]
    解法1: 不推荐! for loop
        x轴文章数量, y轴引用次数, 降序排列. 
        画一下是个递减直方图与f(x)=x的交点, 从大到小最后一个cite>i的就是解
        corner case1: 有一篇0引用文章:
            使得不能enumerate的时候从1开始, 只能从0开始...
            然后比较的时候比较cite和count+1. 
            或者可以理解为, 存在h=0的情况, 所以必须从0开始比较. 
        corner case2: 有一篇1引用文章:
            即循环跳出时是因为循环结束而非cite < i + 1
            这时作为循环变量的i会比实际小1.. !!!!
            所以对于for loop, 需要额外的count.
            while loop则可以直接写?
    
    解法2: while loop
        循环不变量: i [0, N] 因此while循环! 因为for只有[0, N-1]
        TODO: 上面这个判断很重要!!!!
        即i是序号, i+1是篇数. 
        循环跳出时, 刚好是不满足条件的. 即i-1才是idx. i-1对应的篇数是i
        注意while循环跳出是i是大于thresh的, 而range for是等于的...

    解法3: bucket sort, 然后再从大到小
        leetcode discuss的解法是碰巧对的.. 我的解法参照官方solu, 更好一些.
        注意是从y轴循环! 即从y轴下降! 而且是one-by-one下降!
        假设一个bucket里面最多只有一篇paper(total 11增长):
            则代码在y轴一个一个向下尝试, 直到x=y. 即一定能取到==号
        bucket里可能有多本书:
            total可能增长太快, 以至于超过cite, 这里会取到大于号.
    解法3: 
        TODO 一个O(1)space的quick select, 貌似是最快的, 先不写. 
        https://leetcode.com/problems/h-index/discuss/70823/O(N)-time-O(1)space-solution
    """
    # s = Solution()
    # print(s.hIndex([3,0,6,1,5]))
    # print(s.hIndex([100]))
    # print(s.hIndex([0]))
    # print(s.hIndex([1]))
    # print(s.hIndex([5,3,2,2,1]))
