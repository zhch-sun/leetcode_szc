#
# @lc app=leetcode id=127 lang=python
#
# [127] Word Ladder
#
from collections import deque

class Solution(object):
    # def ladderLength(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: int
    #     """
    #     words = set(wordList)
    #     if endWord not in words:
    #         return 0
    #     visited = deque([(beginWord, 1)])
    #     alpha = 'abcdefghijklmnopqrstuvwxyz'

    #     while visited:
    #         word, num_transform = visited.popleft()
    #         for idx in range(len(word)):
    #             for char in alpha:
    #                 # if char != word[idx]:  # 可以省去这个逻辑. 
    #                 tmp = word[:idx] + char + word[idx + 1:]
    #                 if tmp == endWord:
    #                     return num_transform + 1  # 第一个找到的一定是最短的
    #                 if tmp in words:
    #                     visited.append((tmp, num_transform + 1))
    #                     words.remove(tmp)  # 不remove是错的
    #     return 0

    # def ladderLength(self, beginWord, endWord, wordList):
    #     words = set(wordList)
    #     if endWord not in words:
    #         return 0
    #     visited = deque([(beginWord, 1)])  # 可以优化不用steps, 后面循环时注意即可
    #     alpha = 'abcdefghijklmnopqrstuvwxyz'

    #     while visited:
    #         curWord, steps = visited.popleft()
    #         if curWord == endWord:
    #             return steps
    #         for i in range(len(curWord)):
    #             for char in alpha:
    #                 tmp = curWord[:i] + char + curWord[i+1:]
    #                 if tmp in words:
    #                     visited.append((tmp, steps + 1))
    #                     words.remove(tmp)
    #     return 0
    
    def ladderLength(self, beginWord, endWord, wordDict):
        # 从两边搞，生成互斥的三个set front words end。
        words = set(wordDict)
        if endWord not in words:
            return 0
        front = set([beginWord])  # Note 又忘记这个[]了。。。
        end = set([endWord])
        # words.discard(beginWord)  # 隐式保证这个条件，后面会删掉。
        words.discard(endWord)  # 如果想用两头，前面必须删掉end。
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        steps = 1
        while front:
            new_front = set()  # 直接初始化为set而不是list
            for curWord in front:
                for i in range(len(curWord)):
                    for char in alpha:
                        tmp = curWord[:i] + char + curWord[i+1:]
                        if tmp in end:  # 如果要从两边走，必须要这里判断，不能front&end
                            return steps + 1
                        if tmp in words:
                            new_front.add(tmp)
            front = new_front
            words -= front  # set 操作
            if len(front) > len(end):  # 加速: 非常聪明. 
                front, end = end, front 
            steps += 1
        return 0

    # def ladderLength(self, beginWord, endWord, wordDict):
    #     # 用_生成所有的pair.. 不够快. 
    #     def generate_dict(words):
    #         d = {}
    #         for w in words:
    #             for i in range(len(w)):
    #                 s = w[:i] + '_' + w[i+1:]
    #                 d[s] = d.get(s, []) + [w]
    #         return d
                
    #     words = set(wordDict)
    #     if endWord not in words:
    #         return 0
    #     front = set([beginWord])  # Note 又忘记这个[]了。
    #     end = set([endWord])
    #     words_dict = generate_dict(words | front)

    #     words.discard(beginWord)  # 实际上代码里隐式保证这个条件，写上更清晰
    #     words.discard(endWord)  # 如果想用两头，前面必须删掉end。

    #     steps = 1
    #     while front:
    #         if front & end:
    #             return steps
    #         new_front = set()  # 直接初始化为set而不是list
    #         for curWord in front:
    #             for i in range(len(curWord)):
    #                 tmp = curWord[:i] + '_' + curWord[i+1:]
    #                 if tmp in words_dict:
    #                     new_front.update(words_dict[tmp])  # 注意叫update
    #         front = new_front
    #         front = front & (words | end )  # 需要除重且需要过滤end。。
    #         words -= front  # set 操作
    #         if len(front) > len(end):  # 加速
    #             front, end = end, front
    #         steps += 1
    #     return 0

if __name__ == '__main__':
    """
    词语梯子.  所有的word length相同.  没有duplicates. 都是小写26个字母. 
    这个题返回长度, 还有个更难的126返回所有sequence. 这题目有很多优化空间. 
    
    是一个无向图, bfs搜索.
    确实要注意重复情况, 一个词语的25*L条边没有重复, 但是变两次之后就会重复, 所以有
    两个解决方案: 1.搞一个visited set, 存储之前访问过的节点. 2. 每次访问一个就从dict里面删掉. 

    解法1: python里的string是不可修改的, 所以我这里只能重新生成新string 
        beginWord[:idx] + char + beginWord[idx + 1:]. 这样速度太慢了. 
    解法2: 解法1的逻辑不够好. 对于这种题, 每次pop后应该紧跟return条件, 而不是在后面的循环中
        去check条件. 解法1给出正确答案有运气成分.. 前两种解法的好处是空间复杂度很小, 但是for循环很慢. 
    解法3: 两个修改, 1. 内部对alpha的循环改成set操作. 2. 从前后两边forward. 不用queue了. 
        注意python答案里存储所有的front然后front & words的写法更慢。。 应该是没有early stopping了
        然而如果想要front,end = end,front交换的话，一定要循环内部判断是否和end相交。
        这样做实际上把words分为互斥的三部分， front，words，end。所以中间循环如果出现了结果，是
        不会在words里，就找不到任何一个解。而不从两边走的时候，代码保证front和后面互斥就可以
        （隐式执行了words.discard(beginWord)）
    解法4：预先处理wordList，用 _ 代替当前位置，这样避免了后面对每个字符的for循环。
        但是这样并不快。。而且还有若干坑要踩。。。
    """
    s = Solution()
    print(s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
    print(s.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log"]))
