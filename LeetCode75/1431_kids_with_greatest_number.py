class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        most = max(candies)
        for kid in candies:
            result.append(kid + extraCandies >= most)
        return result
