class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        shortest_len = min(len(word) for word in strs)
        for letter_index in range(0, shortest_len):
            letter = strs[0][letter_index]
            for word in strs:
                if word[letter_index] != letter:
                    return prefix

            prefix += letter
        return prefix


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
