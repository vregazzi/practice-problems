class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for ch in [
            '\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+',
            '-', '.', '!', '$', '\'', ':', ',', " ", '@', "{", "}", "\"", "?",
            ";",
        ]:
            s = s.replace(ch, "")

        return s == s[::-1]


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(" ")
    assert not s.isPalindrome("race a car")
    assert s.isPalindrome("A man, a plan, a canal: Panama")
    assert s.isPalindrome("ab@a")
    assert s.isPalindrome("Marge, let's \"[went].\" I await {news} telegram.")
    assert s.isPalindrome("Live on evasions? No, I save no evil.")
    assert s.isPalindrome("I, man, am regal; a German am I.")
