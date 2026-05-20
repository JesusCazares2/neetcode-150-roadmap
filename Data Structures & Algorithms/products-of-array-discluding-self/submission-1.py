class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        i = 0
        while i < len(nums):
            skip_index = i
            remaining_elements = nums[:skip_index] + nums[skip_index + 1:]

            product = math.prod(remaining_elements)
            output.append(product)

            i += 1
        return output