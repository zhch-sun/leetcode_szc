#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
class Solution(object):
    # def groupAnagrams(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: List[List[str]]
    #     """        
    #     from collections import defaultdict
    #     ans = defaultdict(list)
    #     for s in strs:
    #         ans[tuple(sorted(s))].append(s)  # str可以直接sort!
    #     return ans.values()  # TODO 要不要list(ans.values())?

    # def groupAnagrams(self, strs):
    #     res = {}
    #     for s in strs:
    #         key = tuple(sorted(s))  # sorted返回的是list!!!不是string!
    #         res[key] = res.get(key, []) + [s]
    #     return res.values()  # values是个view,意味着res如果变了,values也跟着变

    def groupAnagrams(self, strs):
        from collections import defaultdict
        ans = defaultdict(list)
        for s in strs:
            keys = [0] * 26
            for char in s:
                keys[ord(char) - ord('a')] += 1
            ans[tuple(keys)].append(s)
        return ans.values()

if __name__ == '__main__':
    """
    相同字母异序词
    解法1:
        1. 一个直接的做法是sort每个词, tuple, 然后丢到dict里. 
        2. .values()是个view!
        3. dict的几种用法:
            1. 直接不同dict, 需要处理不存在的情况
            2. get函数
            3. defaultdict.
    解法2：
        利用get处理key可能不存在的情况。
    做法3:
        counting sort节省复杂度. 
        用counter当key变成O(n), 即count sort或者radix sort
        问题是python缺省的counter是实际上是个dict, 而且是无序的. 不能用来当key. 
    """
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
