class Solution:
    start = ["(", "{", "["]
    chars = {
        "(": ")",
        '{': '}',
        '[': ']',
    }

    def isValid(self, s: str) -> bool:
        stack = ""
        for char in s:
            if char in self.start:
                stack = self.chars[char] + stack
            else:
                if len(stack) == 0 or char is not stack[0]:
                    return False
                stack = stack[1:]
        return stack == ""


if __name__ == "__main__":
    s = Solution()
    assert s.isValid("()")
    assert not s.isValid("(]")
    assert not s.isValid("[")
    assert not s.isValid("((")
    assert not s.isValid("]")
