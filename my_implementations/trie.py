from typing import Dict

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Function to insert a word into the trie
    # Time Complexity: O(n), where n is the length of the word
    # Space Complexity: O(n), considering the worst-case scenario where each character of the word is unique
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.

        Trick: Traverse the trie using the characters of the word. Create new nodes if necessary.

        Example Usage: Used to add words to the trie for efficient search operations.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Function to search for a word in the trie
    # Time Complexity: O(n), where n is the length of the word
    # Space Complexity: O(1)
    def search(self, word: str) -> bool:
        """
        Searches for a word in the trie.

        Trick: Traverse the trie using the characters of the word. Return True if the word exists in the trie.

        Example Usage: Used to check if a word exists in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    # Function to delete a word from the trie
    # Time Complexity: O(n), where n is the length of the word
    # Space Complexity: O(1)
    def delete(self, word: str) -> None:
        """
        Deletes a word from the trie.

        Trick: Traverse the trie using the characters of the word. Mark the last node as non-end-of-word.

        Example Usage: Used to remove a word from the trie.
        """
        def _delete_helper(node: TrieNode, word: str, depth: int) -> bool:
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete_current_node = _delete_helper(node.children[char], word, depth + 1)
            if should_delete_current_node:
                del node.children[char]
                return len(node.children) == 0
            return False

        _delete_helper(self.root, word, 0)


# Example usage:
if __name__ == "__main__":
    # Create a new trie instance
    trie = Trie()

    # Insert words into the trie
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")

    # Search for words in the trie
    print("Searching for 'apple':", trie.search("apple"))  # Expected output: True
    print("Searching for 'app':", trie.search("app"))      # Expected output: True
    print("Searching for 'banana':", trie.search("banana"))  # Expected output: True
    print("Searching for 'orange':", trie.search("orange"))  # Expected output: False

    # Delete a word from the trie
    trie.delete("app")
    print("After deleting 'app', searching for 'apple':", trie.search("apple"))  # Expected output: True
    print("After deleting 'app', searching for 'app':", trie.search("app"))      # Expected output: False
