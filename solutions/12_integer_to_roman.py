class Solution:
    def intToRoman(self, num: int) -> str:
        result = "M" * (num // 1000)
        num %= 1000
        result += "D" * (num // 500)
        num %= 500
        result += "C" * (num // 100)
        num %= 100
        result += "L" * (num // 50)
        num %= 50
        result += "X" * (num // 10)
        num %= 10
        result += "V" * (num // 5)
        num %= 5
        result += "I" * num

        return result.replace("DCCCC", "CM") \
            .replace("CCCC", "CD") \
            .replace("LXXXX", "XC") \
            .replace("XXXX", "XL") \
            .replace("VIIII", "IX") \
            .replace("IIII", "IV")


if __name__ == "__main__":
    s = Solution()
    assert s.intToRoman(3749) == "MMMDCCXLIX"
    assert s.intToRoman(58) == "LVIII"
    assert s.intToRoman(1994) == "MCMXCIV"
    assert s.intToRoman(400) == "CD"
