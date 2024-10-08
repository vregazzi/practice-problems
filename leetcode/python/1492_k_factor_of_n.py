class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        updates = 0
        for i in range(1, n + 1):
            if n % i == 0:
                updates += 1
            if k == updates:
                return i
        return -1

    def kthFactor2(self, n: int, k: int) -> int:
        i = 0
        updates = 0

        while updates < k and i <= n:
            i += 1
            if n % i == 0:
                updates += 1

        if k > updates:
            return -1
        return i


if __name__ == "__main__":
    s = Solution()
    assert s.kthFactor(12, 3) == 3
    assert s.kthFactor(7, 2) == 7
    assert s.kthFactor(4, 4) == -1
