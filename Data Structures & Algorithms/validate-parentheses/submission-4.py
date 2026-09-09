class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closed_to_open = {')' : '(',
                          '}' : '{',
                          ']' : '['  
                           }

        for char in s:
            if char in closed_to_open:
                if stack and stack[-1] == closed_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        """
        input: s = "[{()}]"

        output: true

        input: s = "{))[]"

        output: false


        #edge cases

        if empty return:
            false

        #solution

        iterate thru s using a for loop
        stack -> check for a correpsonding close or open bracket.
        return true for valid s and false for every invalid s

        stack = []
        closed_to_open = {
                ) : (,
                } : {,
                ] : [
        }

        input: s = "{))[]"
                        i
        if i is an open bracket:
            we add it to the stack

        else:
            
            #IF THE LAST VAOUE IN THE STACk maps to curr char:
            if "(" maps to ")":
                then pop from the stack
            else:
                we keeo oving i forward

        stack = ['{', ]

        #check for validity of s
        chechk too see ifb the stack is empty:
        we return true
        else:
            we return false


        """
        