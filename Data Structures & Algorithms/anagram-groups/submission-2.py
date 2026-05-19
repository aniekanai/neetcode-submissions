class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      

        #declare a hashmap
        res = defaultdict(list) # mapping charCount to list of Anagrams

        grouped_anagrams = []

        for s in strs:
            count = [0] * 26 # a ... z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        for value in res.values():
            grouped_anagrams.append(value)
        return grouped_anagrams

        
            

