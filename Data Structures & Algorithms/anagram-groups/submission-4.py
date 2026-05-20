class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedGrams = defaultdict(list)

        for word in strs:
            sorted_words = "".join(sorted(word))
            groupedGrams[sorted_words].append(word)

        return list(groupedGrams.values())