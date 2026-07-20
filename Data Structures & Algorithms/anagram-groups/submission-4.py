class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 0:
            return [[]]

        res = []
        str_anag = {}

        for i in range(len(strs)):
            elem = "".join(sorted(strs[i]))

            if elem in str_anag:
                str_anag[elem].append(strs[i])

            else:
                str_anag[elem] = [strs[i]]

        for key in str_anag.keys():
            res.append(str_anag[key])

        return res
                
        
        """
        input: strs = ["tops", "post", "get"]

        output: res = [["tops", "post"], ["get"]]

        input: strs = ["tops", "cab", "get"]

        output: res = [["tops"], ["cab"], ["get"]]



        edge cases:

        if stsrs is empty:
            return [[]]


        #solution

        sorting and hashmaps
        res = []
        dict = {}

        itertae thru strs:
            #sort each elem
            elem = "egt"

            #check if "egt" is in dict:
                #append the curr elem to dict
                dict = {"opst" : ["tops", "post"]}

            #check if "egt" is not in dict:
                #add "egt to dict
                    dict = {"opst", "egt"}
                #give "opst" a value:
                    dict = {"opst": [], "egt" : []}
                #add the curr elem:
                dict = {"opst" : ["tops"], "abc" : ["cab"], "egt" : ["get]}
            
            

        
        itertae thru keys my dict:
            #append all the values of my keys to res
            res = [["tops"], ["cab"], ["get"]]

        return res 

        time complexity = O(n^2 log n)
        space  = O(n)

            





        """
        