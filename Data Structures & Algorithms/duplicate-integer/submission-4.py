class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_vals = set()

        for i in nums:
            if i in seen_vals:
                return True
            else:
                seen_vals.add(i)
        return False