class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            offset = target-num
            if offset in nums[index+1:]:
                return [index, nums.index(offset, index+1)]
        return