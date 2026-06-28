class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, word in zip(pattern, words):
            if c in char_to_word:
                if char_to_word[c] != word:
                    return False
            else:
                char_to_word[c] = word

            if word in word_to_char:
                if word_to_char[word] != c:
                    return False
            else:
                word_to_char[word] = c;

        return True 