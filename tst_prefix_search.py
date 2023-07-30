class TSTNode:
    def __init__(self, char):
        self.char = char
        self.is_end_of_word = False
        self.left = None
        self.middle = None
        self.right = None
        self.words = []


class TST:

    def __init__(self):
        self.root = None
    def print_structure(self):
        def print_recursive(node, level=0, prefix=""):
            if node:
                print(' ' * (level * 4) + '|-- ' + node.char)
                print_recursive(node.left, level + 1, prefix)
                if node.is_end_of_word:
                    print(' ' * ((level + 1) * 4) + '|-- ' +  "#")
                print_recursive(node.middle, level + 1, prefix + node.char)
                print_recursive(node.right, level + 1, prefix)

        print_recursive(self.root)

    def insert(self, word):
        def insert_recursive(node, char_index):
            if char_index == len(word):
                return

            char = word[char_index]

            if not node:
                node = TSTNode(char)

            if char < node.char:
                node.left = insert_recursive(node.left, char_index)
            elif char > node.char:
                node.right = insert_recursive(node.right, char_index)
            else:
                if char_index == len(word) - 1:
                    node.is_end_of_word = True
                else:
                    node.middle = insert_recursive(node.middle, char_index + 1)

            return node

        self.root = insert_recursive(self.root, 0)
    def list_words_with_prefix(self, prefix):
        def traverse_tst(node, current_word, result):
            if not node:
                return

            if node.is_end_of_word:
                result.append(current_word + node.char)

            traverse_tst(node.left, current_word, result)

            traverse_tst(node.middle, current_word + node.char, result)

            traverse_tst(node.right, current_word, result)

        result = []
        prefix_node = self._find_prefix_node(prefix)
        if prefix_node:
            if prefix_node.is_end_of_word:
                result.append(prefix)

            traverse_tst(prefix_node.middle, prefix, result)  # Include the last character of the prefix

        return result
    def _find_prefix_node(self, prefix):
        def find_prefix_recursive(node, char_index):
            if not node:
                return None

            char = prefix[char_index]

            if char < node.char:
                return find_prefix_recursive(node.left, char_index)
            elif char > node.char:
                return find_prefix_recursive(node.right, char_index)
            else:
                if char_index == len(prefix) - 1:
                    return node
                return find_prefix_recursive(node.middle, char_index + 1)

        return find_prefix_recursive(self.root, 0)


# Example usage:
tst = TST()
words = ["apple", "apricot", "banana", "apartment", "apex", "ball", "cat", "dog", "cataract"]

print(words)

for word in words:
    tst.insert(word)

tst.print_structure()
prefix = "ap"
words_with_prefix = tst.list_words_with_prefix(prefix)
print(f"Words with prefix '{prefix}': {words_with_prefix}")

prefix = "ba"
words_with_prefix = tst.list_words_with_prefix(prefix)
print(f"Words with prefix '{prefix}': {words_with_prefix}")
prefix = "cata"
words_with_prefix = tst.list_words_with_prefix(prefix)
print(f"Words with prefix '{prefix}': {words_with_prefix}")
