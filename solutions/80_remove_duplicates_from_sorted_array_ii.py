class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        remove = []
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] and nums[i] == nums[i - 2]:
                remove.append(nums[i])

        for num in remove:
            nums.remove(num)
        return len(nums)
