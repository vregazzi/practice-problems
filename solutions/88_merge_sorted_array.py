class Solution:
    def merge(
            self, nums1: list[int], m: int, nums2: list[int], n: int
            ) -> None:
        for _ in range(n):
            del nums1[-1]

        nums1.extend(nums2)
        nums1.sort()


if __name__ == '__main__':
    s = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1]

    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2]

    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    m = 6
    nums2 = [1, 2, 2]
    n = 3
    s.merge(nums1, m, nums2, n)
    assert nums1 == [-1, 0, 0, 1, 2, 2, 3, 3, 3]

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1]

    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 3, 4, 5, 6]

    nums1 = [-1, -1, 0, 0, 0, 0]
    m = 4
    nums2 = [-1, 0]
    n = 2
    s.merge(nums1, m, nums2, n)
    assert nums1 == [-1, -1, -1, 0, 0, 0]
