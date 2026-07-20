class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_anag = {}
        res = []
        
        for elem in strs:
            arr = [0] * 26
            for i in range(len(elem)):
                arr[ord(elem[i]) - ord('a')] += 1
            key = tuple(arr)

            if key in str_anag:
                str_anag[key].append(elem)
            else:
                str_anag[key] = [elem]
        

        for key in str_anag.keys():
            res.append(str_anag[key])
            

        return res

                


            





  
        