#
# @lc app=leetcode id=546 lang=python
#
# [546] Remove Boxes
#

# @lc code=start
class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        def dfs(i, j, k):
            if (i, j, k) in f:
                return f[i, j, k]
            if i > j:  # =0的情况后面cover
                return 0
            while i < j and boxes[i + 1] == boxes[i]:
                i += 1
                k += 1
            # 用左边和i相同的字母做初始化. 
            # 左边k是0, 右边k是1.
            f[i, j, k] = (k + 1) * (k + 1) + dfs(i + 1, j, 0)
            for idx in xrange(i + 1, j + 1):
                if boxes[idx] == boxes[i]: # 这里需要i仍然指向最初值
                    # 转移方程的第二个部分是k+1啊.
                    f[i, j, k] = max(f[i, j, k], \
                        dfs(i + 1, idx - 1, 0) + dfs(idx, j, k + 1))
            return f[i, j, k]
            
        N = len(boxes)
        f = {}
        return dfs(0, N - 1, 0)  # k表示的是不包含在i,j内的和i相同的个数
        
if __name__ == '__main__':
    """
    这题就是祖玛..
    错解: 和burst ballon一样, 设定一个位置是最后炸.
        但这是错的, 因为需要一个区间最后炸! 比如 1234111. 
        这要求四维dp. 
    解法1: 
        非常详细的答案, 需要全部读完. 
        https://leetcode.com/problems/remove-boxes/discuss/101310/Java-top-down-and-bottom-up-DP-solutions
        思路:
            对于[i,j]区间, 先考虑数i. 只有两种可能, 
            要么自己消, 要么与后面颜色相同的消
                如果没有同样颜色, f[i,j] = 1 + f[i+1,j]
                未来有若干同样颜色 f[i,j] = max(f[i,j], f[idx,j], i+1个第一个数)
                所以递归中需要一个新信息, 有区间外有多少个元素和i位置一样颜色.
        即i, j, k. k表示多少个"区间外"和i位置元素一样的元素将和i一起消失. 
        k引入了是区间的外部信息.
    """
    s = Solution()
    print(s.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))
# @lc code=end
