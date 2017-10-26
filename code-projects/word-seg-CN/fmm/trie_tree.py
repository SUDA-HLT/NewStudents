class TrieTree(object):
    """字典树实现"""
    def __init__(self):
        self.tree = {}

    def add(self, word):
        tree = self.tree
        for char in word:
            if char in tree:
                tree = tree[char]
            else:
                tree[char] = {}
                tree = tree[char]
        tree['exist'] = True

    def search(self, word):
        tree = self.tree
        for char in word:
            if char in tree:
                tree = tree[char]
            else:
                return False

        if 'exist' in tree and tree['exist'] == True:
            return True
        else:
            return False


# tree = TrieTree()
# tree.add('yao ming')
# tree.add('bcd')
# print(tree.tree)
