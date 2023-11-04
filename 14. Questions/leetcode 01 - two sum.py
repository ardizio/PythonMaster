# add two numbers check if target | leetcode 01 | https://leetcode.com/problems/two-sum/
from typing import List

#O(n)^2 solution - brute force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

#O(n) solution - hash maps

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for i, n in enumerate(nums):
            diff = target-n
            if diff in prevMap:
                return[prevMap[diff],i]
            prevMap[n] = i
        return
    



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