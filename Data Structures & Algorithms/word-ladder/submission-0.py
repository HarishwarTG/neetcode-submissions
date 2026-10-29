class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        words, res = set(wordList), 0
        q = collections.deque([beginWord])
        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for c in range(97, 123):
                        if word[i] == chr(c):
                            continue
                        nei = word[:i] + chr(c) + word[i + 1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)
        
        return 0