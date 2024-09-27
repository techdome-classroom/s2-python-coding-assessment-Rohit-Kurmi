class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to map closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Stack to keep track of the opening brackets
        stack = []
        
        # Traverse through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the top element from stack if it is non-empty, otherwise assign a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the top element doesn't match the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it to the stack
                stack.append(char)
        
        # At the end, the stack should be empty for a valid expression
        return not stack





    



  

