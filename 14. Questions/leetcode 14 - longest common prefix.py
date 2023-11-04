"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Questions: https://leetcode.com/problems/longest-common-prefix/

"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""  # Initialize an empty string to store the longest common prefix.
        n = len(strs)  # Get the number of strings in the input list.
        
        # Sort the input list to make it easier to compare the first and last strings.
        strs.sort()
        
        first = strs[0]  # Get the first (lexicographically smallest) string.
        last = strs[n - 1]  # Get the last (lexicographically largest) string.
        
        # Iterate through the characters of the first string.
        for i in range(len(first)):
            # Compare the characters of the first and last strings at the same position.
            if first[i] != last[i]:
                # If a mismatch is found, return the current common prefix.
                return res
            else:
                # If the characters match, append the character to the common prefix.
                res = res + first[i]
        
        # After the loop, return the longest common prefix found.
        return res

        
        

# Test Case 1
# Input: strs = ["flower","flow","flight"]
# Expected Output: "fl" (Common prefix among all strings)
solution = Solution()
result1 = solution.longestCommonPrefix(["flower","flow","flight"])
assert result1 == "fl", "Test Case 1 Failed"

# Test Case 2
# Input: strs = ["dog","racecar","car"]
# Expected Output: "" (No common prefix among the strings)
result2 = solution.longestCommonPrefix(["dog","racecar","car"])
assert result2 == "", "Test Case 2 Failed"

# Test Case 3
# Input: strs = ["apple","appetizer","apparel"]
# Expected Output: "app" (Common prefix among all strings)
result3 = solution.longestCommonPrefix(["apple","appetizer","apparel"])
assert result3 == "app", "Test Case 3 Failed"

# Test Case 4
# Input: strs = ["cat","caterpillar","catamaran"]
# Expected Output: "cat" (Common prefix among all strings)
result4 = solution.longestCommonPrefix(["cat","caterpillar","catamaran"])
assert result4 == "cat", "Test Case 4 Failed"

# Test Case 5
# Input: strs = ["programming","programmer","program"]
# Expected Output: "program" (Common prefix among all strings)
result5 = solution.longestCommonPrefix(["programming","programmer","program"])
assert result5 == "program", "Test Case 5 Failed"

print("All test cases passed!")
