from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.dict    = defaultdict(TrieNode)
        self.is_word = False

class StreamChecker(object):

    def __init__(self, words):
        self.prefix = ""

        self.trie = TrieNode()

        for word in words:
            cur_node = self.trie

            word = word[::-1]

            for char in word:
                cur_node = cur_node.dict[char]

            cur_node.is_word = True

    def query(self, letter):
        self.prefix += letter

        cur_node = self.trie
        for char in reversed(self.prefix):
            if char not in cur_node.dict:
                break

            cur_node = cur_node.dict[char]

            if cur_node.is_word:
                return True

        return False

if __name__ == "__main__":
    streamChecker = StreamChecker(["cd", "f", "kl"])
    print(streamChecker.query('a'))
    print(streamChecker.query('b'))
    print(streamChecker.query('c'))
    print(streamChecker.query('d'))
    print(streamChecker.query('e'))
    print(streamChecker.query('f'))
    print(streamChecker.query('g'))
    print(streamChecker.query('h'))
    print(streamChecker.query('i'))
    print(streamChecker.query('j'))
    print(streamChecker.query('k'))
    print(streamChecker.query('l'))