# add two numbers check if target | leetcode 01 | https://leetcode.com/problems/two-sum/
from typing import List

# O(n^2) solution - brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through the elements in the nums list using two nested loops.
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # Check if the current pair of elements (nums[i] and nums[j]) sum up to the target.
                if nums[i] + nums[j] == target:
                    # If the condition is met, return the indices of the two numbers that add up to the target.
                    return [i, j]
        # If no valid pair is found, return an empty list.
        return []

# O(n) solution - hash maps
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # Create a dictionary to store previously seen numbers and their indices.

        for i, n in enumerate(nums):
            diff = target - n  # Calculate the difference between the target and the current number.
            if diff in prevMap:
                # If the difference exists in the dictionary, it means we found a valid pair.
                # Return the indices of the two numbers that add up to the target.
                return [prevMap[diff], i]
            # If the difference is not in the dictionary, add the current number and its index to the dictionary.
            prevMap[n] = i
        # If no valid pair is found, return an empty list.
        return []

    



# Test Case 1: Brute Force Solution
nums = [2, 7, 11, 15]
target = 9
solution1 = Solution()
output1 = solution1.twoSum(nums, target)
print("Brute Force Solution:", output1) 


# Test Case 2: Hash Maps Solution
nums = [3, 2, 4]
target = 6
solution2 = Solution()
output2 = solution2.twoSum(nums, target)
print("Hash Maps Solution:", output2)