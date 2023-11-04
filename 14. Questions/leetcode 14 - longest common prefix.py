"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Questions: https://leetcode.com/problems/longest-common-prefix/

"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ res = ""
        n = len(strs)
        strs.sort()
        first = strs[0]
        last = strs[n-1]
        for i in range(len(first)):
            if first[i] != last[i]:
                return res
            else:
                res = res + first[i]
        return res """
        res = ""
        print(len(strs))
        print("_______________________________________________")
        return res
        
        
        
#         for i in range(len(strs[0])):
#             for s in strs:
#                 if i == len(s) or s[i] != strs[0][i]:
#                     return res
                
#             res += strs[0][i]
            
#         return res

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
# Expected Output: "pro" (Common prefix among all strings)
result5 = solution.longestCommonPrefix(["programming","programmer","program"])
assert result5 == "pro", "Test Case 5 Failed"

print("All test cases passed!")
