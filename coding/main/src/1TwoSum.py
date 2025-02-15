class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        complement = {}
        for i in range(0,len(nums)):
            comp = target-nums[i]
            for j in range(i+1,len(nums)):
                if comp==nums[j]:
                    output = [i,j]
                    break
        return output
        
