# add two numbers check if target | leetcode 01 | https://leetcode.com/problems/two-sum/

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