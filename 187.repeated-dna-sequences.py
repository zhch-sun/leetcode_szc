#
# @lc app=leetcode id=187 lang=python
#
# [187] Repeated DNA Sequences
#

# @lc code=start
from collections import defaultdict
class Solution(object):
    # def findRepeatedDnaSequences(self, s):
    #     """
    #     :type s: str
    #     :rtype: List[str]
    #     """
    #     N = len(s)
    #     seen = defaultdict(int)
    #     for i in xrange(0, N - 10 + 1):
    #         seen[s[i:i+10]] += 1
    #     return [item for item, val in seen.items() if val > 1]

    def findRepeatedDnaSequences(self, s):
        N = len(s)
        seen = set()
        ans = set()
        for i in xrange(0, N - 10 + 1):
            tmp = s[i: i + 10]
            if tmp in seen:
                ans.add(tmp)
            else:
                seen.add(tmp)
        return list(ans)

if __name__ == '__main__':
    """
    题设: 定长10的子序列, 统计重复的
    解法1:
        一个set. 最后统计一遍cnt>1
    解法2:
        两个set! 快得多. 
    """
    s = Solution()
    print(s.findRepeatedDnaSequences(\
        "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
        
# @lc code=end
