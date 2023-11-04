# longest substring without repeating characters | leetcode 03 | https://leetcode.com/problems/longest-substring-without-repeating-characters
# sliding window; remove elements until last occurence of current duplicate

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize two pointers, ptrL and ptrR, to keep track of the current substring.
        ptrL = 0
        seen = dict()  # Create a dictionary to store characters and their indices.
        longest = 0  # Initialize the variable to keep track of the longest substring length.

        for ptrR in range(len(s)):
            # While the current character (s[ptrR]) is already seen in the substring:
            while seen.get(s[ptrR]) is not None:
                # Remove the character at ptrL from the dictionary and move ptrL rightward.
                seen.pop(s[ptrL])
                ptrL += 1

            # Mark the current character as seen by adding it to the dictionary.
            seen[s[ptrR]] = True

            # Update the longest substring length by comparing with the previous value.
            longest = max(ptrR - ptrL + 1, longest)

        # Return the length of the longest substring with unique characters.
        return longest


                 


# Test Case 1
s1 = "abcabcbb"
solution = Solution()
result1 = solution.lengthOfLongestSubstring(s1)
expected_result1 = 3
assert result1 == expected_result1, f"Expected {expected_result1}, but got {result1}"

# Test Case 2
s2 = "bbbbb"
result2 = solution.lengthOfLongestSubstring(s2)
expected_result2 = 1
assert result2 == expected_result2, f"Expected {expected_result2}, but got {result2}"

# Test Case 3
s3 = "pwwkew"
result3 = solution.lengthOfLongestSubstring(s3)
expected_result3 = 3
assert result3 == expected_result3, f"Expected {expected_result3}, but got {result3}"

print("All test cases passed!")