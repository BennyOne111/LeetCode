class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.is_end
            ch = word[index]
            if ch == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])  
        
        return dfs(0, self)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)