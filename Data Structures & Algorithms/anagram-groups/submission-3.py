from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped_anagrams = []
        sorted_anagrams = defaultdict(list)

        for word in strs:

            sorted_word = "".join(sorted(word))

            if sorted_word not in sorted_anagrams:
                sorted_anagrams[sorted_word].append(word)

            else:
                sorted_anagrams[sorted_word].append(word)

        for val in sorted_anagrams.values():
            grouped_anagrams.append(val)

        return grouped_anagrams
                
        """
        input: ["cat", "act", "key", "bread]

        output: [["cat", "act"], ["key"], ["bread"]]

        
        Edge case
        input: [""]
        output: [[""]]


        Solution:

        hashmap
        grouped_anagrams = []

        sorted_anagrams = {}
        # ["cat", "act", "key", "bread]
                                   ^
        iterate through strs:
        for "bread" in my array(strs): -> O(n) where n is the no of elements in strs

            sorted_word = "".join(sorted(bread) = "abder" -> O(klogk) where k is avg length of each char

            #abder not in dictionary
            if "abder" not in sorted_anagrams:
                sorted_anagrams = { "act" : ["cat", "act"]
                                    "eky" : ["key"]
                                    "abder" :
                                        }

            map the word "key" to "eky" in dictionary
            sorted_anagrams = { "act" : ["cat", "act"]
                                "eky" : ["key"]
                                "abder" : ["bread"]

                                        }

        for val in my dictionary values:

            grouped_anagrams = [["cat", "act"],  ["key"], ["bread"]]
                                
        time -> O(n.klogk) + O(n) = O(n * klogk)
        space -> O(n * k)
        return grouped_anagrams

        """

