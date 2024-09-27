class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        for char in s:
            if char in stack:
                break
            stack.append(char)

        return len(stack)


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert False
