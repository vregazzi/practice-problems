class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        remove = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                remove.append(nums[i])

        for num in remove:
            nums.remove(num)
        return len(nums)
