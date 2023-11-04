"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.

Question: https://leetcode.com/problems/palindrome-number/

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Check if the given number is negative, which cannot be a palindrome.
        if x < 0:
            return False

        c = x  # Create a copy of the input number.
        b = 0  # Initialize a variable to store the reverse of the number.

        # Reverse the number.
        while c:
            # shift b by one and add last c digit to it
            b = b * 10 + c % 10
            #print("C:",c," - B:",b)
            # integer dision to remove the last digit of a number
            c //= 10

        # Check if the reversed number is equal to the original number.
        return b == x

        


# Test Case 1: Positive Palindrome
# Input: x = 121
# Expected Output: True (121 is a palindrome)
solution = Solution()
result1 = solution.isPalindrome(121)
assert result1 == True, "Test Case 1 Failed"

# Test Case 2: Negative Number
# Input: x = -121
# Expected Output: False (-121 is not a palindrome)
result2 = solution.isPalindrome(-121)
assert result2 == False, "Test Case 2 Failed"

# Test Case 3: Non-Palindrome
# Input: x = 12345
# Expected Output: False (12345 is not a palindrome)
result3 = solution.isPalindrome(12345)
assert result3 == False, "Test Case 3 Failed"

# Test Case 4: Single Digit
# Input: x = 7
# Expected Output: True (Single digits are considered palindromes)
result4 = solution.isPalindrome(7)
assert result4 == True, "Test Case 4 Failed"

# Test Case 5: Zero
# Input: x = 0
# Expected Output: True (Zero is a palindrome)
result5 = solution.isPalindrome(0)
assert result5 == True, "Test Case 5 Failed"

print("All test cases passed!")
