class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        fake_list = nums.copy()
        k = k % len(nums)
        for i in range(0, len(nums)):
            nums[i] = fake_list[i - k]


s = Solution()
s.rotate([-1], 2)
