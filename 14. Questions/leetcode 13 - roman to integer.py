"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Questions: https://leetcode.com/problems/roman-to-integer/

"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        res = 0
        
        for i in range(len(s)):
            # check if next exitst   and check if roman nox < roman now+1
            if i+1 <len(s) and roman[s[i]] < roman[s[i+1]]:
                # tolgo il risultato attuale
                res -=  roman[s[i]]
            else:
                res += roman[s[i]]
        return res
    

# Test Case 1
# Input: s = "III"
# Expected Output: 3 (III represents 3 in Roman numerals)
solution = Solution()
result1 = solution.romanToInt("III")
assert result1 == 3, "Test Case 1 Failed"

# Test Case 2
# Input: s = "LVIII"
# Expected Output: 58 (LVIII represents 58 in Roman numerals)
result2 = solution.romanToInt("LVIII")
assert result2 == 58, "Test Case 2 Failed"

# Test Case 3
# Input: s = "MCMXCIV"
# Expected Output: 1994 (MCMXCIV represents 1994 in Roman numerals)
result3 = solution.romanToInt("MCMXCIV")
assert result3 == 1994, "Test Case 3 Failed"

print("All test cases passed!")
