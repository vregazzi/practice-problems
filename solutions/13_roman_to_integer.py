class Solution:
    nums = {"I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            if (i != len(s) - 1 and self.nums[s[i]] < self.nums[s[i + 1]]):
                total -= self.nums[s[i]]
                continue
            total += self.nums[s[i]]
        return total


if __name__ == "__main__":
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    assert s.romanToInt("MCDLXXVI") == 1476
    assert s.romanToInt("DCXXI") == 621
