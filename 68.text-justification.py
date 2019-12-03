#
# @lc app=leetcode id=68 lang=python
#
# [68] Text Justification
#

# @lc code=start
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans, cur = [], []  # cur line
        cur_len = 0
        for w in words:
            # 注意还要加上空格数! 但是len(cur)不减1
            if cur_len + len(w) + len(cur) > maxWidth:  
                for i in xrange(maxWidth - cur_len):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                ans.append(''.join(cur))
                cur = []
                cur_len = 0
            cur.append(w)
            cur_len += len(w)
        # 一定有额外的值.
        ans.append(' '.join(cur).ljust(maxWidth))
        return ans

if __name__ == '__main__':
    """
    解法1:
        核心的空格安排方法, 
        其实是Round-Robin(字面意思是循环赛): 轮流放置
        即每个数放到下一个结点上, 并循环.
    """
    s = Solution()
    print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
    print(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"], 20))
    
        
# @lc code=end

