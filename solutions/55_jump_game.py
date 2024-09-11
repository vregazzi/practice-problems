class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if nums[0] == 0 and len(nums) != 1:
            return False

        dist_from_back = -1

        while dist_from_back > -1 * len(nums):  # until we reach index 0
            for i in range(1, len(nums)):
                if nums[-i - 1] >= i:
                    dist_from_back = -i - 1
                    nums = nums[:-i]
                    break
                if i + 1 == len(nums):
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4])
    assert not s.canJump([3, 2, 1, 0, 4])
    assert s.canJump([0])
    assert s.canJump([2, 5, 0, 0])
    assert not s.canJump([0, 1])
    assert s.canJump([2, 0])
    assert s.canJump([2, 0, 0])
    assert s.canJump([1, 1, 1, 0])
    assert s.canJump([3, 0, 8, 2, 0, 0, 1])
    assert not s.canJump([0, 2, 3])
