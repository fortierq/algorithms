class Trie:
    def __init__(self, words):
        self.word = None
        self.childs = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        t = self
        for c in word:
            if c not in t.childs:
                t.childs[c] = Trie([])
            t = t.childs[c]
        t.word = word
    
    def __contains__(self, word):
        t = self
        for c in word:
            if c not in t.childs:
                return False
            t = t.childs[c]
        return t.word is not None

    def words(self):
        t = self
        if t.word:
            yield t.word
        for c in t.childs.values():
            yield from c.words()

    def startswith(self, prefix):
        t = self
        s = set()
        for c in prefix:
            if c not in t.childs:
                return s
            t = t.childs[c]
        yield from t.words()
