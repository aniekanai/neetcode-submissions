class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #nlogn algorithm

        #declare a hashmap
        word_anagrams = {}

        #declare a list
        grouped_anagrams = []

        #iterate through the array

        for word in strs:
            #sort the word
            word_sorted = "".join(sorted(word))
            if word_sorted in word_anagrams:
                word_anagrams[word_sorted].append(word)
            else:
                word_anagrams[word_sorted] = []
                word_anagrams[word_sorted].append(word)
                

           
        for value in word_anagrams.values():
            grouped_anagrams.append(value)

        return grouped_anagrams
            

