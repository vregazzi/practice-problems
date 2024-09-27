class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        count = min(len(str1), len(str2))
        i = 0
        divisor = ""
        while i < count and str1[i] == str2[i]:
            divisor += str1[i]
            i += 1

        str1_len = len(str1)
        str2_len = len(str2)
        div_len = len(divisor)

        if not div_len:
            return ""

        if str1_len % div_len != 0 or str2_len % div_len != 0:
            divisor = divisor[:(div_len // 2)]

        return divisor


if __name__ == "__main__":
    s = Solution()
    # assert s.gcdOfStrings("", "") == ""
    assert s.gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert s.gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert s.gcdOfStrings("ABCDEF", "ABC") == "ABC"
