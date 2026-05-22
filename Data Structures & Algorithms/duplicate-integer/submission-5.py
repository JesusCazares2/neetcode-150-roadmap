class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_val = set()

        for i in nums:
            if i in seen_val:
                return True
            seen_val.add(i)
        return False