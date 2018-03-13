from queue import Queue

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        graph = self.build_graph(beginWord, endWord, wordList)
        return self.BFS(graph, beginWord, endWord)

    def BFS(self, graph, beginWord, endWord):
        length = len(graph) + 1
        q = Queue()
        q.put_nowait([beginWord, 1])
        visited = {}
        visited[beginWord] = 1
        while q.qsize() > 0:
            word, step = q.get_nowait()
            # print(q.qsize())
            for neighbor in graph[word]:
                if neighbor == endWord:
                    if step + 1 < length:
                        length = step + 1
                if neighbor not in visited:
                    visited[neighbor] = 1
                    q.put_nowait([neighbor, step + 1])
        if length == len(graph) + 1:
            return 0
        return length


    def build_graph(self, beginWord, endWord, wordList):
        listing = wordList
        listing.insert(0, beginWord)
        graph = {}
        for i in range(len(listing)):
            for j in range(i + 1, len(listing)):
                w = listing[i]
                n = listing[j]
                connected = self.diff(listing[i], listing[j])
                if w not in graph:
                    graph[w] = []
                if connected:
                    graph[w].append(n)
                    if n not in graph:
                        graph[n] = []
                    graph[n].append(w)
        return graph

    def diff(self, w, v):
        d = 0
        for i in range(len(w)):
            if w[i] != v[i]:
                d += 1
            if d >= 2:
                return False
        if d == 1:
            return True
        return False


if __name__ == '__main__':
    S = Solution()
    print(S.ladderLength('hit', 'cog',["hot","dot","dog","lot","log","cog"]))