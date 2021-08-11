class Trie:
    """Tree where each node represents a letter...TODO: write propper docstring..."""

    class _Node:
        """Non-public Node subclass for Trie class"""

        def __init__(self, letter=None, is_word=False):
            """Create Trie node instance"""
            self.letter = letter
            self.is_word = is_word
            self.children = {}

    def __init__(self):
        """Initialise instance of Trie class and set root"""
        self.root = self._Node()

    def add_word(self, word):
        """Adds word string to the Trie tree"""
        index_node = self.root
        is_word = False
        for letter_index, letter in enumerate(word):
            if letter not in index_node.children:
                if letter_index == len(word) - 1:    # if iter is last letter
                    is_word = word                   # store whole word in node
                index_node.children[letter] = self._Node(
                    letter, is_word)                 # add new node in child dict
            elif letter_index == len(word) - 1:
                index_node.children[letter].is_word = word
            # move index node to new child
            index_node = index_node.children[letter]

    def find_words(self, user_letters):
        """Returns set of words in Trie with matching user letters"""
        self.found_words = []   # create or clear list for matching words
        user_letters_dict = {}  # create dict of user letters e.g 'a':3
        for letter in user_letters:
            if letter not in user_letters_dict:
                user_letters_dict[letter] = 1
            else:
                user_letters_dict[letter] += 1
        self._find_words(user_letters_dict)
        return self.found_words

    # --- Private methods:

    def _find_words(self, user_letters, node=None):
        """Appends to self.found_words list all words added to Trie instance that can be made using user_letters"""
        if node == None:
            node = self.root
        if node.is_word:
            self.found_words.append(node.is_word)
        # Base case:
        if len(node.children) == 0 or sum(user_letters.values()) == 0:
            return
        # else recur down each node.child where node.child in user_letters and count > 0
        for child in node.children:
            if child in user_letters and user_letters[child] > 0:
                user_letters_less_child = user_letters.copy()
                user_letters_less_child[child] -= 1
                self._find_words(user_letters_less_child, node.children[child])


word_list = ['cat', 'cold', 'cot', 'colt', 'car', 'card', 'coat',
             'coddle', 'cod', 'cool', 'old', 'odd', 'bold', 'cheese', 'do']

trie = Trie()

for word in word_list:
    trie.add_word(word)

user_letters = 'dogcat'

print(trie.find_words(user_letters))
