class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in seenNums:
                return [seenNums[difference], i]
            seenNums[n] = i