class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack.__contains__(needle):
            return -1
        return haystack.index(needle)


if __name__ == "__main__":
    s = Solution()
    assert s.strStr("sadbutsad", "sad") == 0
    assert s.strStr("leetcode", "leeto") == -1
