class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)

        return [item[0] for item in frequency_map.most_common(k)]
            
    
       