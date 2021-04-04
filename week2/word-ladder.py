#题目：单词接龙
#原解法：回溯，超时了
# class Solution:
#     def is_valid(self,word1,word2):
#         count = 0
#         for i in range(len(word1)):
#             if word1[i]!=word2[i]:
#                 count += 1
#         if count <= 1:
#             return True
#         else:
#             return False

#     def backtracking(self,begin_word,end_word,word_list,path,used,res):
#         if path[-1]==end_word:
#             res['len'] = min(res['len'],len(path))
#             return
#         if len(path) >= res['len']:
#             return
#         for i in range(len(word_list)):
#             if not used[i] and self.is_valid(path[-1],word_list[i]):
#                 used[i] = True
#                 self.backtracking(begin_word,end_word,word_list,path+[word_list[i]],used,res)
#                 used[i] = False
#         return
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0
        
#         used = [False for i in range(len(wordList))]
#         res = {'len':float('inf')}
#         path = [beginWord]
#         self.backtracking(beginWord,endWord,wordList,path,used,res)
#         return 0 if res['len']==float('inf') else res['len']

#参考官方题解使用了图的广度优先遍历+优化建图，
# 稍微优化了一下官方edge原先用list的方式（会加入重复元素），改为set去重
import collections
class Solution:
    def __init__(self):
        self.node_num = 0
        self.word_ids = {}
        self.edge = collections.defaultdict(set)
    
    def add_word(self,word):
        if word not in self.word_ids:
            self.node_num += 1
            self.word_ids[word] = self.node_num

    def add_edge(self,word):
        self.add_word(word)
        word1_id = self.word_ids[word]
        word1_char = list(word)
        for i in range(len(word1_char)):
            tmp = word1_char[i]
            word1_char[i] = '*'
            new_word1 = ''.join(word1_char)
            self.add_word(new_word1)
            new_word1_id = self.word_ids[new_word1]
            self.edge[word1_id].add(new_word1_id)
            self.edge[new_word1_id].add(word1_id)
            word1_char[i] = tmp


    def ladderLength(self, beginWord, endWord, wordList) -> int:
        if endWord not in wordList:
            return 0
        #self.add_word(beginWord)
        self.add_edge(beginWord)
        for word in wordList:
            self.add_edge(word)
        print(self.word_ids)
        print(self.edge)
        #图的遍历
        que = collections.deque()
        que.append(self.word_ids[beginWord])
        vis = set([self.word_ids[beginWord]])
        end_word_id = self.word_ids[endWord]
        step = 0
        while que:
            que_size = len(que)
            for i in range(que_size):
                word_id = que.popleft()
                if word_id == end_word_id:
                    return step // 2 +1
                vis.add(word_id)
                edges = self.edge[word_id]
                for e in edges:
                    if e not in vis:
                        que.append(e)
            step += 1
        return 0  #找不到要返回0 

#双向bfs解法
#import string
#print(string.ascii_lowercase)
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        front = {beginWord}
        back = {endWord}
        wordList = set(wordList) #这句一定要加上!!!!!,list和set的查找效率大概是几十倍的差距
        dis = 1
        while front:
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i+1:] #加1不要忘了
                            if new_word in back:
                                return dis + 1
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            dis += 1
            front = next_front
            if len(front) > len(back):
                front,back = back,front                           
        return 0


