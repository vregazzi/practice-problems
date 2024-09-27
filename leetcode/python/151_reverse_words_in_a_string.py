class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        while "  " in s:
            s = s.replace("  ", " ")
        words = s.split(" ")
        words.reverse()
        return " ".join(words)


if __name__ == "__main__":
    s = Solution()
    assert s.reverseWords("the sky is blue") == "blue is sky the"
    assert s.reverseWords("  hello world  ") == "world hello"
    assert s.reverseWords("a good   example") == "example good a"
