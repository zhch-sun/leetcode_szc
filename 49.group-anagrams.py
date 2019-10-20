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
    #     res = {}
    #     for s in strs:
    #         key = ''.join(sorted(s))  # TODO 这里应该用tuple
    #         if key in res:
    #             res[key].append(s)
    #         else:
    #             res[key] = [s]
    #     return res.values()

    # def groupAnagrams(self, strs):
    #     res = {}
    #     for s in strs:
    #         key = tuple(sorted(s))  # sorted返回的是list!!!不是string!
    #         res[key] = res.get(key, []) + [s]
    #     return res.values()  # values是个view,意味着res如果变了,values也跟着变
        
    def groupAnagrams(self, strs):
        # 97
        import collections
        res = collections.defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))  # sorted返回的是list!!!不是string!
            res[key].append(s)
        return res.values()  # values是个view,意味着res如果变了,values也跟着变

    # def groupAnagrams(self, strs):
    #     res = {}
    #     for s in strs:
    #         key = [0] * 26
    #         for char in s:
    #             key[ord(char) - ord('a')] += 1
    #         key = tuple(key)
    #         res[key] = res.get(key, []) + [s]
    #     return res.values()

if __name__ == '__main__':
    """
    相同字母异序词
    做法1:
    1. 一个直接的做法是sort每个词, tuple, 然后丢到dict里. 
    3. .values()是个view!
    解法2：
    利用get处理key可能不存在的情况。
    做法3 
    defaultdict:对于这种不停get的,可以直接搞defaultdict!!!
    做法4:
    用counter当key变成O(n), 即count sort或者radix sort
    问题是python缺省的counter是实际上是个dict, 而且是无序的. 不能用来当key. 
    """
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
