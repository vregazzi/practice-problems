class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for flower in flowerbed:
            if not flower:
                n -= 1

        return n == 0


if __name__ == "__main__":
    s = Solution()
    assert s.canPlaceFlowers([1, 0, 0, 0, 1], 1)
    assert not s.canPlaceFlowers([1, 0, 0, 0, 1], 2)
    assert False