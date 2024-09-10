class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split(" ")
        word_list.reverse()

        while word_list[0] == "":
            word_list.remove("")

        return len(word_list[0])


s = Solution()
w = "   fly me   to   the moon  "
print(s.lengthOfLastWord(w))
