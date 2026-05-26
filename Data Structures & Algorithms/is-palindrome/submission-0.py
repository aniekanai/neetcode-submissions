class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 0:
            return True
        # s = "tab a cat"
        cleaned_s = "".join(char for char in s.lower() if char.isalnum())
        #cleaned = "tabacat" -> 7 letters
        print(cleaned_s)
        
        i = 0
        j = len(cleaned_s) - 1 # 6

        # i = 2
        # j = 4
        # "tabacat"
        #    ^ ^
        #    i j

        while i < j:
            #checks for non-identical chars
            if cleaned_s[i] != cleaned_s[j]:
                print(cleaned_s[i])
                print(cleaned_s[j])
                #s is not a palindrome
                return False

            i += 1
            j -= 1

        #s is a palindrome
        return True
        """

        "mom" -> "mom" -> true

        "bad" -> "dab" -> false

        edge case:

        empty string
        input: ""
        output: True

        case-sensitive
        input: "Mom"
        convert to lowercase 
        solve
        output: True

        special characters
        input: "man a nam"
        strip the string of any special characters
        solve
        output: True

        Solution

            Visualization

            two pointer approach

            input: "man a nam"

            for odd input lengths
            strip_input -> mananam - 7 letters 
                        ^     ^
                            i   j while i < j
            input: "man nam"
            strip: "mannam" -> 6 letters
                    ^    ^
                    i    j

            time_complexity O(n)
            space_complexity -> O(1)

            """

            


