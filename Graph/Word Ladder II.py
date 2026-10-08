class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []
        
        visited = {beginWord}
        found = False

        queue = deque([beginWord])
        parent = defaultdict(list)

        while queue and not found:
            level_seen = set()

            for _ in range(len(queue)):
                word = queue.popleft()

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        nxt = word[:i] + ch + word[i+1:]

                        if nxt not in wordSet or nxt in visited:
                            continue
                        
                        parent[nxt].append(word)
                        
                        if nxt not in level_seen:
                            level_seen.add(nxt)
                            queue.append(nxt)
                        
                        if nxt == endWord:
                            found = True
            
            visited.update(level_seen)
        
        if not found:
            return []
        
        ans = []
        path = [endWord]

        def dfs(word):

            if word == beginWord:
                ans.append(path[::-1])
                return
            
            for prev in parent[word]:
                path.append(prev)
                dfs(prev)
                path.pop()
        
        dfs(endWord)
        return ans


        