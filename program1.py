class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to map Roman numerals to their integer values
        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # Traverse the string
        for i in range(n):
            # If the current numeral is less than the next, subtract it
            if i < n - 1 and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                # Otherwise, add its value
                total += roman[s[i]]
        
        return total
