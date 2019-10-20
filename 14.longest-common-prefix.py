#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = ''
        for pair in zip(*strs):
            if len(set(pair)) > 1:
                break
            else:
                ret += pair[0]
        return ret
    
    # def longestCommonPrefix(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #     """
    #     if not strs: return ""
    #     if len(strs) == 1: return strs[0]
        
    #     strs.sort()
    #     p = ""
    #     for x, y in zip(strs[0], strs[-1]):
    #         if x == y: p+=x
    #         else: break
    #     return p

if __name__ == '__main__':
    """
    use sort to only check the 1st and last str. 但是sort太慢了
    应该还是zip的方法更好？
    TODO need to understand that. like binary search..？？？有新解法吗？
    sort itself might not be a good way because it scans all the strings.
    """
    s = Solution()
    print(s.longestCommonPrefix(['sa1', 'saaa2']))

