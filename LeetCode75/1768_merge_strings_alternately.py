class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = min(len(word1), len(word2))
        new_word = ""
        for i in range(0, count):
            new_word += word1[i]
            new_word += word2[i]

        new_word += word1[count:]
        new_word += word2[count:]

        return new_word


if __name__ == "__main__":
    s = Solution()
    assert s.mergeAlternately("", "") == ""
    assert s.mergeAlternately("abc", "pqr") == "apbqcr"
    assert s.mergeAlternately("ab", "pqrs") == "apbqrs"
